from abc import ABC

from TicTacToe.Game.task import TicTacToe


class DotsAndBoxes(TicTacToe, ABC):
    def __init__(self, board):
        super().__init__(board)

    def get_next_state(self, board, player, action):
        # if a player takes action on board, return next (board,player)
        # action must be a valid move
        pass # TODO: implement the get_next_state method, where the last action stands for the pass

    def change_perspective(self, board, player):
        pass # TODO: implement change_perspective method
