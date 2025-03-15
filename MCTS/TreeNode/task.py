import math
import numpy as np

from TicTacToe.Board.task import Board


class Node:
    def __init__(self, game, args, board_state, parent=None, action_taken=None):
        # game (TicTacToe in our case)
        self.game = game
        # some hyperparameters
        self.args = args
        self.state = board_state
        self.parent = parent
        self.action_taken = action_taken

        # make sure that action_taken is None only for root
        if parent is None:
            assert action_taken is None
        if action_taken is None:
            assert parent is None

        self.children = []
        # add calculation for expandable moves
        self.expandable_moves = None # implement calculation for expandable moves

        # The number of times the node has been visited during the simulation phase of MCTS
        self.visit_count = 0
        # The accumulated score associated with that node.
        self.value_sum = 0

    def get_player(self):
        # use state to get the current player. If no action was taken, then player should be None
        pass # return player for this node

    def is_fully_expanded(self):
        # check if this node cannot be expanded
        pass # check if the node is fully expanded

    def select(self):
        pass # return the best child using UCB formula

    def get_ucb(self, child):
        # we want to put the opponent in a bad position, so invert the score
        q_value = 1 - ((child.value_sum / child.visit_count) + 1) / 2
        return q_value + self.args['C'] * math.sqrt(math.log(self.visit_count) / child.visit_count)

    def expand(self):
        # implement expansion step
        pass # implement expansion step, return new child for the node

    def simulate(self):
        # implement simulation step
        pass # simulate random game from the current node

    def backpropagate(self, value):
        # implement a backpropagation step.
        # Hint: do not forget to switch value when passing it to the parent
        pass # implement backpropagation step
