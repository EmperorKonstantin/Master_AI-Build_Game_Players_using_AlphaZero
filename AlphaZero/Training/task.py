import numpy as np
import random
import torch
import torch.nn.functional as F

from TicTacToe.Board.task import Board
from TicTacToe.Game.task import TicTacToe
from ResNetEstimator.Model.task import ResNet
from AlphaZero.SelfPlay.task import AlphaZero


class AlphaZeroTrainer(AlphaZero):
    def __init__(self, model, optimizer, game, args):
        super().__init__(model, optimizer, game, args)

    def self_play(self):
        memory = []
        player = 1
        state = self.game.get_board().create_new_board()

        while True:
            neutral_state = self.game.change_perspective(state, player)
            action_probs = self.mcts.search(neutral_state)

            memory.append((neutral_state, action_probs, player))

            valid_moves = neutral_state.get_valid_moves()
            action_probs *= valid_moves
            action_probs /= np.sum(action_probs)

            # TODO: add action choosing with temperature

            value = self.game.get_game_ended(state, player)

            if value:
                return_memory = []
                for hist_neutral_state, hist_action_probs, hist_player in memory:
                    hist_outcome = value if hist_player == player else self.game.get_opponent_value(value)
                    return_memory.append((
                        hist_neutral_state.get_encoded_state(),
                        hist_action_probs,
                        hist_outcome
                    ))
                return return_memory

            player = self.game.get_opponent(player)

    def train(self, memory):
        random.shuffle(memory)
        for batchIdx in range(0, len(memory), self.args['batch_size']):
            # TODO: implement training loop
            self.optimizer.step()


args = {
    'C': 2,
    'num_searches': 60,
    'num_iterations': 3,
    'num_self_play_iterations': 500,
    'num_epochs': 4,
    'temperature': 1.25,
    'batch_size': 32,
}


def main():
    tictactoe = TicTacToe(Board())
    device = torch.device(
        "cuda"
        if torch.cuda.is_available()
        else "mps"
        if torch.backends.mps.is_available()
        else "cpu"
    )
    model = ResNet(tictactoe, 4, 64, device=device)
    optimizer = torch.optim.Adam(
        model.parameters(), lr=0.001, weight_decay=0.0001
    )
    alphaZero = AlphaZeroTrainer(model, optimizer, tictactoe, args)
    alphaZero.learn()


if __name__ == '__main__':
    main()
