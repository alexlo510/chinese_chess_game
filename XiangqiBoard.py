# Author: Alex Lo
# Date: 3/3/2020
# Description:

from XiangqiPieces import General, Advisor, Elephant, Horse, Chariot, Cannon, Soldier


class BoardPoints:
    """Represents the intersections of the rows and columns on the board."""
    def __init__(self, row, column):
        """Initializes private data members."""
        self._row = row
        self. column = column
        self._piece_on_point = ""  # add a null piece?
        self._occupied = False
        self._location = (row, column)

    def get_piece_on_point(self):
        """Returns the piece on the point."""
        return self._piece_on_point

    def set_piece_on_point(self, game_piece_object):
        """Takes a game piece object and sets piece on point to the game piece. Sets occupied to True"""
        self._piece_on_point = game_piece_object
        self._occupied = True

    def remove_piece_on_point(self):
        """Sets piece on point to "" and sets occupied to False."""
        self._piece_on_point = ""
        self._occupied = False

    def get_location(self):
        """Returns the location."""
        return self._location

    def is_occupied(self):
        """Returns is occupied."""
        return self._occupied

    def set_occupied(self, occupied_status):
        """Updates the self.occupied."""
        self._occupied = occupied_status


class Board:
    """Represents a Board"""

    def __init__(self):
        """Initializes private data members."""
        # initialize a 2D array to represent an empty 9x10 board (9 rows, 10 columns) and create a BoardPoints object in
        # each of the column and row spaces.
        self._board = [[BoardPoints(rows, columns) for columns in range(0, 9)] for rows in range(0, 10)]

        # add the pieces on the board at their starting positions.

        # pieces at row 0
        self.add_piece("red", "chariot", 0, 0)
        self.add_piece("red", "horse", 0, 1)
        self.add_piece("red", "elephant", 0, 2)
        self.add_piece("red", "advisor", 0, 3)
        self.add_piece("red", "general", 0, 4)
        self.add_piece("red", "advisor", 0, 5)
        self.add_piece("red", "elephant", 0, 6)
        self.add_piece("red", "horse", 0, 7)
        self.add_piece("red", "chariot", 0, 8)

        # pieces at row 2
        self.add_piece("red", "cannon", 2, 1)
        self.add_piece("red", "cannon", 2, 7)

        # pieces at row 3
        self.add_piece("red", "soldier", 3, 0)
        self.add_piece("red", "soldier", 3, 2)
        self.add_piece("red", "soldier", 3, 4)
        self.add_piece("red", "soldier", 3, 6)
        self.add_piece("red", "soldier", 3, 8)

        # pieces at row 6
        self.add_piece("black", "soldier", 6, 0)
        self.add_piece("black", "soldier", 6, 2)
        self.add_piece("black", "soldier", 6, 4)
        self.add_piece("black", "soldier", 6, 6)
        self.add_piece("black", "soldier", 6, 8)

        # pieces at row 7
        self.add_piece("black", "cannon", 7, 1)
        self.add_piece("black", "cannon", 7, 7)

        # pieces at row 9
        self.add_piece("black", "chariot", 9, 0)
        self.add_piece("black", "horse", 9, 1)
        self.add_piece("black", "elephant", 9, 2)
        self.add_piece("black", "advisor", 9, 3)
        self.add_piece("black", "general", 9, 4)
        self.add_piece("black", "advisor", 9, 5)
        self.add_piece("black", "elephant", 9, 6)
        self.add_piece("black", "horse", 9, 7)
        self.add_piece("black", "chariot", 9, 8)

    def display_board(self):
        """Prints the board."""
        for row in range(0, 10):
            print("[", end="")
            for column in range(0, 9):
                if column == 8:
                    print(self._board[row][column].get_piece_on_point(), end="")
                elif column == 0:
                    if self._board[row][column].get_piece_on_point() == "":
                        print(self._board[row][column].get_piece_on_point(), end=" , ")
                    else:
                        print(self._board[row][column].get_piece_on_point(), end=", ")
                else:
                    print(self._board[row][column].get_piece_on_point(), end=", ")
            print("]")

    def add_piece(self, color, piece_type, row, column):
        """Takes a color, piece_type string, row, and column and adds a specific GamePiece object to the BoardPoint."""
        add = self._board[row][column].set_piece_on_point
        if piece_type.lower() == "general":
            add(General(color, piece_type, row, column))
        elif piece_type.lower() == "advisor":
            add(Advisor(color, piece_type, row, column))
        elif piece_type.lower() == "elephant":
            add(Elephant(color, piece_type, row, column))
        elif piece_type.lower() == "horse":
            add(Horse(color, piece_type, row, column))
        elif piece_type.lower() == "chariot":
            add(Chariot(color, piece_type, row, column))
        elif piece_type.lower() == "cannon":
            add(Cannon(color, piece_type, row, column))
        elif piece_type.lower() == "soldier":
            add(Soldier(color, piece_type, row, column))

    def get_board_point(self, row, column):
        """Returns a BoardPoint Object"""
        return self._board[row][column]

    def get_red_general_location(self):
        """Returns the location of the red general"""
        for row in range(0, 10):
            for column in range(0, 9):
                if self.get_board_point(row, column).is_occupied() is True:
                    if self.get_board_point(row, column).get_piece_on_point().get_game_piece_color() == "red":
                        if self.get_board_point(row, column).get_piece_on_point().get_piece_type() == "general":
                            return self.get_board_point(row, column).get_location()

    def get_black_general_location(self):
        """Returns the location of the black general"""
        for row in range(0, 10):
            for column in range(0, 9):
                if self.get_board_point(row, column).is_occupied() is True:
                    if self.get_board_point(row, column).get_piece_on_point().get_game_piece_color() == "black":
                        if self.get_board_point(row, column).get_piece_on_point().get_piece_type() == "general":
                            return self.get_board_point(row, column).get_location()

