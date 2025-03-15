import matplotlib.pyplot as plt
import torch

from TicTacToe.Board.task import Board
from TicTacToe.Game.task import TicTacToe
from TicTacToe.Round.task import Round
from ResNetEstimator.Model.task import ResNet


def init_and_apply_nn(round):
    pass # Implement model initialization with parameters `num_res_blocks = 4, num_hidden = 64` and apply it to get the value_item and policy_probs


def main():
    third_round = Round(TicTacToe(Board()))
    # player 1
    third_round.play_game(2)
    # player -1
    third_round.play_game(7)
    print("Current game board is:")
    third_round.print_game_layout()
    encoded_state = third_round.instance_of_game.get_board().get_encoded_state()
    print(f"Encoded state = \n{encoded_state}")
    value, policy_probs = init_and_apply_nn(third_round)
    print(f"Value = {value}, \npolicy_probs = {policy_probs}")
    plt.bar(range(third_round.instance_of_game.get_board().get_action_size()), policy_probs)
    plt.show()


if __name__ == '__main__':
    main()
