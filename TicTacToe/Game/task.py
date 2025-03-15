import math
from abc import ABC

from GameInterface import Game


class TicTacToe(Game, ABC):
    def __init__(self, board):
        self._board = None # Init with Board instance

    def get_board(self):
        return self._board

    def get_next_state(self, board, player, action):
        board.execute_move(player, action)
        return board

    def get_valid_moves(self):
        return self._board.get_valid_moves()

    def get_game_ended(self, board, player):
        # Return 1 if player is win, -1 if -player is win (that means player is loose), 0 if where are legal moves
        # draw has a very little positive reward
        return 1e-4

    def get_canonical_form(self, player):
        # return state if player==1, else return -state if player==-1
        return player * self._board

    def get_opponent(self, player):
        # Return the opponent player
        return -player

    def get_opponent_value(self, value):
        return value if math.isclose(value, 1e-4) else -value

    def change_perspective(self, board, player):
        board_changed = None # Change 1 to -1 and vice versa for -1 player and save it in changed_board
        return board_changed
