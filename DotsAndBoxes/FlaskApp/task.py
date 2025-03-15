import os
from abc import ABC

import torch
from flask import Flask, render_template, request, jsonify

from DotsAndBoxes.Board.task import BoardDandB
from DotsAndBoxes.Backend.task import Backend
from ResNetEstimator.Model.task import ResNet

args = {
    'C': 2,
    'num_searches': 60,
    'num_iterations': 3,
    'num_self_play_iterations': 100,
    'num_epochs': 25,
    'temperature': 1.25,
    'batch_size': 64,
}

device = torch.device(
    "cuda"
    if torch.cuda.is_available()
    else "mps"
    if torch.backends.mps.is_available()
    else "cpu"
)

# Constants for the game
SIZE_OF_WINDOW = 600
PLAYER1_COLOR = '#6c57fb'  # Blue
PLAYER2_COLOR = '#20d689'  # Green
PLAYER1_COLOR_LIGHT = '#a291ff'  # Light Blue
PLAYER2_COLOR_LIGHT = '#65ecb7'  # Light Green


class FlaskApp(ABC):
    def __init__(self, backend):
        self.backend = backend

        self.number_of_dots = (self.backend.num_rows + self.backend.num_cols) // 2 + 1
        self.distance_between_dots = SIZE_OF_WINDOW / self.number_of_dots

        self.app = Flask(__name__)
        self.setup_routes()

    def setup_routes(self):
        @self.app.route('/')
        def index():
            return render_template('index.html')

        @self.app.route('/play_again', methods=['POST'])
        def play_again():
            self.backend.refresh()
            return jsonify(success=True)

        @self.app.route('/click', methods=['POST'])
        def click():
            is_cur_player1, edge_type, logical_position = None, None, []
            success = False
            data = request.json
            # TODO: set grid_position with click coordinates
            player1 = self.backend.player1
            player2 = self.backend.player2
            if (not self.backend.agent_play
                    or (self.backend.agent_play and self.backend.player1_turn)):
                if grid_position == [0, 0]:
                    self.backend.emulate_next_move = False
                else:
                    self.backend.emulate_next_move = True
                # TODO: convert coordinates to logical position
                if edge_type and not self.backend.is_edge_occupied(edge_type, logical_position):
                    is_cur_player1 = self.backend.player1_turn
                    success = True

                    # TODO: update board and perform action
            elif self.backend.agent_play and not self.backend.player1_turn:
                is_cur_player1 = self.backend.player1_turn
                edge_type, logical_position = self.backend.agent_move()
                success = True
                if self.backend.is_gameover():
                    self.backend.emulate_next_move = False

            # TODO: prepare edge_data and player_data for the response
            cell_data = {
                'cell_status': self.backend.cell_status.tolist()
            }
            return jsonify(success=success, edge_data=edge_data,
                           player_data=player_data, cell_data=cell_data)

    def run(self):
        model = ResNet(self.backend, 4, 64, device=device)
        model_num = args['num_iterations'] - 1
        filename = f'../TrainAndPlay/models/model_{model_num}.pt'

        if os.path.exists(filename):
            model.load_state_dict(torch.load(filename, map_location=device))
            model.eval()
            self.backend.agent = model
            self.backend.agent_play = True
            self.backend.player2 = "AlphaZero"

        self.app.run(debug=False, port=8080)


def main():
    game_backend = Backend(BoardDandB())
    app = FlaskApp(game_backend)
    app.run()


if __name__ == "__main__":
    main()
