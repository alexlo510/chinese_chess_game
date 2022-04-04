# Author: Alex Lo
# Date: 3/3/2020
# Description:


class GamePiece:
    """Represents a Xiangqi Piece"""

    def __init__(self, color, piece_type, row, column):
        """"""
        self._color = color
        self._piece_type = piece_type
        self._location = (row, column)

    def __repr__(self):
        """"""
        pass

    def __str__(self):
        """"""
        return str(self._color).upper() + " " + str(self._piece_type).upper()

    def get_game_piece_color(self):
        """Returns game piece color"""
        return self._color

    def get_piece_type(self):
        """Returns game piece type"""
        return self._piece_type

    def set_location(self, row, column):
        """Sets the location of the piece."""
        self._location = (row, column)


class General(GamePiece):
    """"""

    def __init__(self, color, piece_type, row, column):
        """"""
        super().__init__(color, piece_type, row, column)

    def possible_moves(self):
        """Takes a parameter of the current row and current column and returns a list of possible moves. Note:
        does not mean the move is valid."""
        list_of_possible_moves = []
        current_row = self._location[0]
        current_column = self._location[1]

        # boundary limits of a red general.
        if self.get_game_piece_color() == "red":
            min_row = 0
            max_row = 2
            min_column = 3
            max_column = 5

        # boundary limits of a black general.
        else:
            min_row = 7
            max_row = 9
            min_column = 3
            max_column = 5

        for next_row_index in range(-1, 2):  # the piece can potentially move one row ahead or behind.
            for next_column_index in range(-1, 2):  # the piece can potentially move one column ahead or behind
                possible_row_move = current_row + next_row_index
                possible_column_move = current_column + next_column_index

                if possible_row_move < min_row or possible_row_move > max_row:
                    continue
                elif possible_column_move < min_column or possible_column_move > max_column:
                    continue

                # the piece would already be in the location. No need to append to list.
                elif possible_row_move == current_row and possible_column_move == current_column:
                    continue

                # will handle if the possible move is already occupied later.

                list_of_possible_moves.append((possible_row_move, possible_column_move))

        return list_of_possible_moves


class Advisor(GamePiece):
    """"""

    def __init__(self, color, piece_type, row, column):
        """"""
        super().__init__(color, piece_type, row, column)

    def possible_moves(self):
        """Takes a parameter of the current row and current column and returns a list of possible moves. Note:
        does not mean the move is valid."""
        list_of_possible_moves = []
        current_row = self._location[0]
        current_column = self._location[1]
        slope = [-1, 1]  # the advisor can move diagonally, so the slope is either -1 or 1.

        # boundary limits of a red advisor.
        if self.get_game_piece_color() == "red":
            min_row = 0
            max_row = 2
            min_column = 3
            max_column = 5

        # boundary limits of a black advisor.
        else:
            min_row = 7
            max_row = 9
            min_column = 3
            max_column = 5

        for next_row_index in range(-1, 2):  # the piece can potentially move one row ahead or behind.
            for next_column_index in range(-1, 2):  # the piece can potentially move one column ahead or behind
                possible_row_move = current_row + next_row_index
                possible_column_move = current_column + next_column_index

                if possible_row_move < min_row or possible_row_move > max_row:
                    continue
                elif possible_column_move < min_column or possible_column_move > max_column:
                    continue

                # to not get an error in division when calculating the slope.
                if possible_column_move - current_column == 0:
                    continue
                # calculate the slopes of the possible row and column moves.
                if (possible_row_move - current_row)/(possible_column_move - current_column) not in slope:
                    continue

                list_of_possible_moves.append((possible_row_move, possible_column_move))

        return list_of_possible_moves


class Elephant(GamePiece):
    """"""

    def __init__(self, color, piece_type, row, column):
        """"""
        super().__init__(color, piece_type, row, column)

    def possible_moves(self):
        """Takes a parameter of the current row and current column and returns a list of possible moves. Note:
        does not mean the move is valid."""
        list_of_possible_moves = []
        current_row = self._location[0]
        current_column = self._location[1]
        slope = [-1, 1]  # the elephant can move diagonally, so the slope is either -1 or 1.

        # boundary limits of a red elephant. cannot move across river.
        if self.get_game_piece_color() == "red":
            min_row = 0
            max_row = 4
            min_column = 0
            max_column = 8

        # boundary limits of a black elephant.
        else:
            min_row = 5
            max_row = 9
            min_column = 0
            max_column = 8

        for next_row_index in range(-2, 3, 2):  # the piece can potentially move two row ahead or behind.
            for next_column_index in range(-2, 3, 2):  # the piece can potentially move two column ahead or behind
                possible_row_move = current_row + next_row_index
                possible_column_move = current_column + next_column_index

                if possible_row_move < min_row or possible_row_move > max_row:
                    continue
                elif possible_column_move < min_column or possible_column_move > max_column:
                    continue

                # to not get an error in division when calculating the slope.
                if possible_column_move - current_column == 0:
                    continue
                # calculate the slopes of the possible row and column moves.
                if (possible_row_move - current_row)/(possible_column_move - current_column) not in slope:
                    continue

                list_of_possible_moves.append((possible_row_move, possible_column_move))

        return list_of_possible_moves


class Horse(GamePiece):
    """"""

    def __init__(self, color, piece_type, row, column):
        """"""
        super().__init__(color, piece_type, row, column)

    def possible_moves(self):
        """Takes a parameter of the current row and current column and returns a list of possible moves. Note:
        does not mean the move is valid."""
        list_of_possible_moves = []
        current_row = self._location[0]
        current_column = self._location[1]
        # the Horse can move one point orthogonally and one point diagonally, so the slope is either -1 or 1.
        slope = [0.5, -0.5, 2, -2]
        min_row = 0
        max_row = 9
        min_column = 0
        max_column = 8

        for next_row_index in range(-2, 3):  # the piece can potentially move up to two row ahead or behind.
            for next_column_index in range(-2, 3):  # the piece can potentially move up to two column ahead or behind
                possible_row_move = current_row + next_row_index
                possible_column_move = current_column + next_column_index

                if possible_row_move < min_row or possible_row_move > max_row:
                    continue
                elif possible_column_move < min_column or possible_column_move > max_column:
                    continue

                # to not get an error in division when calculating the slope.
                if possible_column_move - current_column == 0:
                    continue
                # calculate the slopes of the possible row and column moves.
                if (possible_row_move - current_row) / (possible_column_move - current_column) not in slope:
                    continue

                list_of_possible_moves.append((possible_row_move, possible_column_move))

        return list_of_possible_moves


class Chariot(GamePiece):
    """"""

    def __init__(self, color, piece_type, row, column):
        """"""
        super().__init__(color, piece_type, row, column)


class Cannon(GamePiece):
    """"""

    def __init__(self, color, piece_type, row, column):
        """"""
        super().__init__(color, piece_type, row, column)


class Soldier(GamePiece):
    """"""

    def __init__(self, color, piece_type, row, column):
        """"""
        super().__init__(color, piece_type, row, column)
