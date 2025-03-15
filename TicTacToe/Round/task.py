from TicTacToe.Board.task import Board
from TicTacToe.Game.task import TicTacToe


class Round:
    def __init__(self, instance_of_game):
        self.instance_of_game = instance_of_game
        self.player = 1

    def print_game_layout(self):
        print(self.instance_of_game.get_board())
        valid_moves = self.instance_of_game.get_valid_moves()
        # Print the list of valid moves

    def play_game(self, action):
        valid_moves = self.instance_of_game.get_valid_moves()
        # If action is not valid, print "action not valid" and exit the function with True return value

        self.instance_of_game._board = None # Update the board according to user's action

        value = self.instance_of_game.get_game_ended(
            self.instance_of_game.get_board(), self.player
        )

        # Check the status of the game. Print the result and exit the function if game ends

        self.player = None # Update player using get_opponent method and exit the function


def main():
    first_round = Round(TicTacToe(Board()))
    is_playing = True
    while is_playing:
        first_round.print_game_layout()
        choose = int(input())
        is_playing = first_round.play_game(choose)


if __name__ == '__main__':
    main()
