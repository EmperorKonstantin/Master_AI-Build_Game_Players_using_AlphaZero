import numpy as np

EMPTY = 0
WHITE = 1
BLACK = -1


class Board:
    """
    Board class for the game of TicTacToe.
    The default board size is 3x3.
    Board data:
      1=white(O), -1=black(X), 0=empty
      first dim is row, second is column:
         pieces[0][0] is the top left square,
         pieces[2][0] is the bottom left square,
    Squares are stored and manipulated as (x,y) tuples.

    Based on the board for the game of TicTacToe by Evgeny Tyurin, github.com/evg-tyurin
    """
    def __init__(self, num_rows: int = 3, num_cols: int = 3):
        """Set up the initial board configuration"""
        self._num_rows = num_rows
        self._num_cols = num_cols
        # Create an empty board (numpy 2-dimensional array)
        # Create numpy array with EMPTY elements
        self._pieces = np.full((self._num_rows, self._num_cols), None)

    def get_board_size(self):
        return self._num_rows * self._num_cols

    def get_action_size(self):
        return self._num_rows * self._num_cols

    def create_new_board(self):
        return Board(self._num_rows, self._num_cols)

    def copy(self):
        """Create a deep copy of the board"""
        board = Board(self._num_rows, self._num_cols)
        board.pieces = np.copy(self.pieces)
        return board

    def __getitem__(self, index):
        i, j = index
        return # Element with i,j index

    def __setitem__(self, index, value):
        i, j = index
        # Assign value to element with i,j index

    @property
    def pieces(self):
        return self._pieces

    @pieces.setter
    def pieces(self, value):
        self._pieces = value

    @property
    def size(self):
        return self._num_cols

    def has_valid_moves(self) -> bool:
        pass # True, if at least one element is EMPTY. False otherwise

    def get_valid_moves(self):
        pass # Implement get_valid_moves function

    def is_win(self, player: int) -> bool:
        """Check whether the given player has collected a triplet in any direction on a rectangular board"""
        pass # Implement is_win function

    def execute_move(self, player: int, action: int):
        """Perform the given action on the board"""
        pass # Implement execute_move function

    def __str__(self):
        board_str = []
        for x in range(self._num_rows):
            for y in range(self._num_cols):
                piece = self[x, y]
                if piece == WHITE:
                    board_str.append("X")
                elif piece == BLACK:
                    board_str.append("O")
                elif piece == EMPTY:
                    board_str.append("-")
            board_str.append("\n")
        return "".join(board_str)

    def get_encoded_state(self):
        encoded_state = None # numpy stack of three masks
        return encoded_state

    def get_player(self, action):
        row = action // self.size
        column = action % self.size
        return self[row, column]
