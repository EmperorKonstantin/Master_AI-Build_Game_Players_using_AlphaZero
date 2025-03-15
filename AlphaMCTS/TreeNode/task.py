import numpy as np
import math


class Node:
    def __init__(self, game, args, board_state, parent=None, action_taken=None, prior=0):
        # game (TicTacToe in our case)
        self.game = game
        # some hyperparameters
        self.args = args
        self.state = board_state
        self.parent = parent
        self.action_taken = action_taken
        self.prior = prior

        # make sure that action_taken is None only for root
        if parent is None:
            assert action_taken is None
        if action_taken is None:
            assert parent is None

        self.children = []
        self.expandable_moves = board_state.get_valid_moves()

        self.visit_count = 0
        self.value_sum = 0

    def get_player(self):
        # use state to get the current player. If no action was taken, then player should be None
        if self.action_taken is None:
            return None
        return self.state.get_player(self.action_taken)

    def is_fully_expanded(self):
        return len(self.children) > 0

    def select(self):
        best_child = None
        best_ucb = -np.inf

        for child in self.children:
            ucb = self.get_ucb(child)
            if ucb > best_ucb:
                best_child = child
                best_ucb = ucb

        return best_child

    def get_ucb(self, child):
        pass # TODO: implement UCB score, accounting for child probability from the model and the border case with child.visit_count = 0

    def expand(self, policy):
        pass # TODO: expansion step for all the children

    def backpropagate(self, value):
        self.value_sum += value
        self.visit_count += 1

        value = self.game.get_opponent_value(value)
        if self.parent is not None:
            self.parent.backpropagate(value)
