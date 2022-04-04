# Author: Alex Lo
# Date: 3/9/2020
# Description: A class named XiangqiGame that is used for playing an abstract board game called Xiangqi. The XiangqiGame
#              class includes a method called get_game_state, is_in_check, and make_move.The players can make a move in
#              the game by using the make_move method, get the game state using the get_game_state method, and check if
#              a general is in check with the is_in_check method. The game is over when a player cannot make a move
#              without leaving their general in check. The XiangqiGame class has a Board class. The Board class has
#              BoardPoints class. The BoardPoints class has GamePiece class.


class GamePiece:
    """Represents a Xiangqi game piece"""

    def __init__(self, color, piece_type, row, column):
        """Initializes private data members: color, piece_type, and location."""
        self._color = color
        self._piece_type = piece_type
        self._location = (row, column)

    def __repr__(self):
        """Returns unambiguous representation of all the data in the object."""
        return "GamePiece(" + self._color + ", " + self._piece_type + ", " + str(self._location[0]) + ", " + \
               str(self._location[1]) + ")"

    def __str__(self):
        """Returns informal readable representation of the object."""
        return str(self._color).upper() + " " + str(self._piece_type).upper()

    def get_game_piece_color(self):
        """Returns game piece color"""
        return self._color

    def get_piece_type(self):
        """Returns game piece type"""
        return self._piece_type

    def set_location(self, row, column):
        """Takes a row and column as integers and changes the location of the piece."""
        self._location = (row, column)


class General(GamePiece):
    """Represents a general game piece with inheritance from GamePiece."""

    def __init__(self, color, piece_type, row, column):
        """Makes use of GamePiece's init method."""
        super().__init__(color, piece_type, row, column)

    def __repr__(self):
        """Returns unambiguous representation of all the data in the object. Overrides GamePiece's repr method."""
        return "General(" + self._color + ", " + self._piece_type + ", " + str(self._location[0]) + ", " + \
               str(self._location[1]) + ")"

    def possible_moves(self):
        """Uses the piece's location and returns a list of possible moves. Note: does not mean the move is valid, does
        not take in account if the location is already occupied."""
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

                # if the row is out of bounds.
                if possible_row_move < min_row or possible_row_move > max_row:
                    continue
                # if the column is out of bounds.
                elif possible_column_move < min_column or possible_column_move > max_column:
                    continue
                # the piece would already be in the location. No need to append to list.
                elif possible_row_move == current_row and possible_column_move == current_column:
                    continue

                list_of_possible_moves.append((possible_row_move, possible_column_move))

        return list_of_possible_moves


class Advisor(GamePiece):
    """Represents an advisor game piece with inheritance from GamePiece."""

    def __init__(self, color, piece_type, row, column):
        """Makes use of GamePiece's init method."""
        super().__init__(color, piece_type, row, column)

    def __repr__(self):
        """Returns unambiguous representation of all the data in the object. Overrides GamePiece's repr method."""
        return "Advisor(" + self._color + ", " + self._piece_type + ", " + str(self._location[0]) + ", " + \
               str(self._location[1]) + ")"

    def possible_moves(self):
        """Uses the piece's location and returns a list of possible moves. Note: does not mean the move is valid, does
        not take in account if the location is already occupied."""
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

                # if the row is out of bounds.
                if possible_row_move < min_row or possible_row_move > max_row:
                    continue
                # if the column is out of bounds.
                elif possible_column_move < min_column or possible_column_move > max_column:
                    continue
                # to not get an error in division when calculating the slope.
                elif possible_column_move - current_column == 0:
                    continue
                # calculate the slopes of the possible row and column moves.
                elif (possible_row_move - current_row)/(possible_column_move - current_column) not in slope:
                    continue

                list_of_possible_moves.append((possible_row_move, possible_column_move))

        return list_of_possible_moves


class Elephant(GamePiece):
    """Represents an elephant game piece with inheritance from GamePiece."""

    def __init__(self, color, piece_type, row, column):
        """Makes use of GamePiece's init method."""
        super().__init__(color, piece_type, row, column)

    def __repr__(self):
        """Returns unambiguous representation of all the data in the object. Overrides GamePiece's repr method."""
        return "Elephant(" + self._color + ", " + self._piece_type + ", " + str(self._location[0]) + ", " + \
               str(self._location[1]) + ")"

    def possible_moves(self):
        """Uses the piece's location and returns a list of possible moves. Note: does not mean the move is valid, does
        not take in account if the location is already occupied."""
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
    """Represents a horse game piece with inheritance from GamePiece."""

    def __init__(self, color, piece_type, row, column):
        """Makes use of GamePiece's init method."""
        super().__init__(color, piece_type, row, column)

    def __repr__(self):
        """Returns unambiguous representation of all the data in the object. Overrides GamePiece's repr method."""
        return "Horse(" + self._color + ", " + self._piece_type + ", " + str(self._location[0]) + ", " + \
               str(self._location[1]) + ")"

    def possible_moves(self):
        """Uses the piece's location and returns a list of possible moves. Note: does not mean the move is valid, does
        not take in account if the location is already occupied."""
        list_of_possible_moves = []
        current_row = self._location[0]
        current_column = self._location[1]
        # the horse can move one point orthogonally and one point diagonally, the slope is either 0.5, -0.5, 2, or -2.
        slope = [0.5, -0.5, 2, -2]
        min_row = 0
        max_row = 9
        min_column = 0
        max_column = 8

        for next_row_index in range(-2, 3):  # the piece can potentially move up to two row ahead or behind.
            for next_column_index in range(-2, 3):  # the piece can potentially move up to two column ahead or behind
                possible_row_move = current_row + next_row_index
                possible_column_move = current_column + next_column_index

                # if the row is out of bounds
                if possible_row_move < min_row or possible_row_move > max_row:
                    continue
                # if the column is out of bounds
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
    """Represents a chariot game piece with inheritance from GamePiece."""

    def __init__(self, color, piece_type, row, column):
        """Makes use of GamePiece's init method."""
        super().__init__(color, piece_type, row, column)

    def __repr__(self):
        """Returns unambiguous representation of all the data in the object. Overrides GamePiece's repr method."""
        return "Chariot(" + self._color + ", " + self._piece_type + ", " + str(self._location[0]) + ", " + \
               str(self._location[1]) + ")"


class Cannon(GamePiece):
    """Represents a chariot game piece with inheritance from GamePiece."""

    def __init__(self, color, piece_type, row, column):
        """Makes use of GamePiece's init method."""
        super().__init__(color, piece_type, row, column)

    def __repr__(self):
        """Returns unambiguous representation of all the data in the object. Overrides GamePiece's repr method."""
        return "Cannon(" + self._color + ", " + self._piece_type + ", " + str(self._location[0]) + ", " + \
               str(self._location[1]) + ")"


class Soldier(GamePiece):
    """Represents a soldier game piece with inheritance from GamePiece."""

    def __init__(self, color, piece_type, row, column):
        """Makes use of GamePiece's init method."""
        super().__init__(color, piece_type, row, column)

    def __repr__(self):
        """Returns unambiguous representation of all the data in the object. Overrides GamePiece's repr method."""
        return "Soldier(" + self._color + ", " + self._piece_type + ", " + str(self._location[0]) + ", " + \
               str(self._location[1]) + ")"


class NonePiece(GamePiece):
    """Represents not having a game piece with inheritance from GamePiece."""

    def __init__(self, color, piece_type, row, column):
        """Makes use of GamePiece's init method."""
        super().__init__(color, piece_type, row, column)

    def __repr__(self):
        """Returns unambiguous representation of all the data in the object. Overrides GamePiece's repr method."""
        return "NonePiece(" + self._color + ", " + self._piece_type + ", " + str(self._location[0]) + ", " + \
               str(self._location[1]) + ")"

    def __str__(self):
        """Returns informal representation of the object. Overrides GamePiece's str method."""
        return ""


class BoardPoints:
    """Represents the intersections of the rows and columns on the board."""
    def __init__(self, row, column):
        """Initializes private data members: row, column, piece on point as a NonePiece object, occupied as False, and
        location as a tuple using row and column. The NonePiece object is initialized with color as None, piece type as
        None, and the row and column being the same as the BoardPoints's."""
        self._row = row
        self. column = column
        self._piece_on_point = NonePiece(None, None, row, column)
        self._occupied = False
        self._location = (row, column)

    def get_piece_on_point(self):
        """Returns the piece on the point."""
        return self._piece_on_point

    def set_piece_on_point(self, game_piece_object):
        """Takes a game piece object and sets piece on point to the game piece. Sets occupied to True"""
        self._piece_on_point = game_piece_object
        self._occupied = True

    def remove_piece_on_point(self, row, column):
        """Takes a row and a column and sets piece on point to NonePiece with color as None, piece type as None, row
        as the row argument, and column as the column argument. Sets occupied to False."""
        self._piece_on_point = NonePiece(None, None, row, column)
        self._occupied = False

    def get_location(self):
        """Returns the location."""
        return self._location

    def is_occupied(self):
        """Returns data member occupied."""
        return self._occupied

    def set_occupied(self, occupied_status):
        """Takes either True or False and updates the occupied data member."""
        self._occupied = occupied_status


class Board:
    """Represents a Board"""

    def __init__(self):
        """Initializes private data member: board as a 9x10 board with a BoardPoints object on each row and column.
         Adds a piece on the the BoardPoint object at specific locations on the board."""
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
                    if isinstance(self._board[row][column].get_piece_on_point(), NonePiece):
                        print(self._board[row][column].get_piece_on_point(), end=" , ")
                    else:
                        print(self._board[row][column].get_piece_on_point(), end=", ")
                else:
                    print(self._board[row][column].get_piece_on_point(), end=", ")
            print("]")

    def add_piece(self, color, piece_type, row, column):
        """Takes a color(string), piece_type(string), row(int), and column(int) and adds a specific GamePiece object to
         the BoardPoint."""
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
        else:
            return False
        return True

    def get_board_point(self, row, column):
        """Takes a row and column as integers and returns a BoardPoint Object"""
        return self._board[row][column]

    def get_red_general_location(self):
        """Returns the location of the red general"""
        # iterate through the board
        for row in range(0, 10):
            for column in range(0, 9):
                # if the board point is occupied
                if self.get_board_point(row, column).is_occupied() is True:
                    # if the piece at the board point is red
                    if self.get_board_point(row, column).get_piece_on_point().get_game_piece_color() == "red":
                        # if the piece at the board point is a general type
                        if self.get_board_point(row, column).get_piece_on_point().get_piece_type() == "general":
                            return self.get_board_point(row, column).get_location()

    def get_black_general_location(self):
        """Returns the location of the black general"""
        # iterate through the board
        for row in range(0, 10):
            for column in range(0, 9):
                # if the board point is occupied
                if self.get_board_point(row, column).is_occupied() is True:
                    # if the piece at the board point is black
                    if self.get_board_point(row, column).get_piece_on_point().get_game_piece_color() == "black":
                        # if the piece at the board point is a general type
                        if self.get_board_point(row, column).get_piece_on_point().get_piece_type() == "general":
                            return self.get_board_point(row, column).get_location()


class XiangqiGame:
    """Represents a Xiangqi game."""

    def __init__(self):
        """Initializes private data members: game_state as "UNFINISHED", game_board as a Board object, and players
        turn as "red"."""
        self._game_state = "UNFINISHED"
        self._game_board = Board()
        self._players_turn = "red"

    def display_game_board(self):
        """Returns the game board object calling its display_board method. This returns a printed board."""
        return self._game_board.display_board()

    def get_game_state(self):
        """Returns the state of the game. Will either be "UNFINISHED", "RED_WON", or "BLACK_WON"."""
        return self._game_state

    def make_move(self, move_from, move_to):
        """Takes a string algebraic notation and returns True if the move is made and moves the piece and False if the
        move can't be made. If the move leaves the opponent in a checkmate or stalemate. Changes the game status."""

        list_of_column_positions = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
        list_of_row_positions = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]

        if self._game_state != "UNFINISHED":
            return False
        # if the algebraic notation for the column is not on the board.
        if move_to[0].lower() not in list_of_column_positions or move_from[0].lower() not in list_of_column_positions:
            return False
        # if the algebraic notation for the row is not on the board.
        elif move_to[1:].lower() not in list_of_row_positions or move_from[1:].lower() not in list_of_row_positions:
            return False

        # translate algebraic notation to row and column index
        row_move_from_index = list_of_row_positions.index(move_from[1:])
        column_move_from_index = list_of_column_positions.index(move_from.lower()[0])
        row_move_to_index = list_of_row_positions.index(move_to[1:])
        column_move_to_index = list_of_column_positions.index(move_to.lower()[0])

        # if there is no piece to get valid moves from.
        if self._game_board.get_board_point(row_move_from_index, column_move_from_index).is_occupied() is False:
            return False

        move_from_game_piece = self._game_board.get_board_point(row_move_from_index, column_move_from_index).\
            get_piece_on_point()

        # if the piece color that is attempting the move not the same as the players turn.
        if move_from_game_piece.get_game_piece_color() != self._players_turn:
            return False

        # get the piece's move list from get_valid_moves method.
        valid_move_list = self.get_valid_moves(row_move_from_index, column_move_from_index)

        if valid_move_list is False:
            return False
        # if black is already in check and the piece making the move is black.
        elif self.is_in_check("black") is True and move_from_game_piece.get_game_piece_color() == "black":
            # check if the black general will still be in check after moving using test_move_in_check method.
            valid_move_list = self.test_move_in_check(row_move_from_index, column_move_from_index, valid_move_list)
            if (row_move_to_index, column_move_to_index) in valid_move_list:
                # move game piece to new position
                self._game_board.get_board_point(row_move_to_index, column_move_to_index).\
                    set_piece_on_point(move_from_game_piece)
                # update the game piece location to the new position
                self._game_board.get_board_point(row_move_to_index, column_move_to_index).get_piece_on_point().\
                    set_location(row_move_to_index, column_move_to_index)
                # remove game piece from old position
                self._game_board.get_board_point(row_move_from_index, column_move_from_index).\
                    remove_piece_on_point(row_move_from_index, column_move_from_index)

                # change the players turn to red after the move is made.
                self._players_turn = "red"
                return True
            else:
                return False
        # if red is already in check and the piece making the move is red.
        elif self.is_in_check("red") is True and move_from_game_piece.get_game_piece_color() == "red":
            # check if the red general will still be in check after moving using test_move_in_check method.
            valid_move_list = self.test_move_in_check(row_move_from_index, column_move_from_index, valid_move_list)
            if (row_move_to_index, column_move_to_index) in valid_move_list:
                # move game piece to new position
                self._game_board.get_board_point(row_move_to_index, column_move_to_index).\
                    set_piece_on_point(move_from_game_piece)
                # update the game piece location to the new position
                self._game_board.get_board_point(row_move_to_index, column_move_to_index).get_piece_on_point().\
                    set_location(row_move_to_index, column_move_to_index)
                # remove game piece from old position
                self._game_board.get_board_point(row_move_from_index, column_move_from_index).\
                    remove_piece_on_point(row_move_from_index, column_move_from_index)

                # change the players turn to black after the move is made.
                self._players_turn = "black"
                return True
            else:
                return False
        # if the move is valid and no one is in check.
        elif (row_move_to_index, column_move_to_index) in valid_move_list:
            # move game piece to new position
            self._game_board.get_board_point(row_move_to_index, column_move_to_index).\
                set_piece_on_point(move_from_game_piece)
            # update the game piece location to the new position
            self._game_board.get_board_point(row_move_to_index, column_move_to_index).get_piece_on_point().\
                set_location(row_move_to_index, column_move_to_index)
            # remove game piece from old position
            self._game_board.get_board_point(row_move_from_index, column_move_from_index).\
                remove_piece_on_point(row_move_from_index, column_move_from_index)

            if self._players_turn == "red":
                self._players_turn = "black"
            elif self._players_turn == "black":
                self._players_turn = "red"

            # check for checkmate and stalemate
            if move_from_game_piece.get_game_piece_color() == "red":
                # Checking for checkmate, if after doing the move, it makes the other general in check.
                is_checkmate_or_stalemate = None
                # test all the moves that the black pieces have
                for row in range(0, 10):
                    for column in range(0, 9):
                        if self._game_board.get_board_point(row, column).is_occupied() is True:
                            if self._game_board.get_board_point(row, column).get_piece_on_point(). \
                                    get_game_piece_color() == "black":
                                # test that piece's moves to see if after they do the move, is the black general in
                                # check using test_move_game_won method.
                                is_checkmate_or_stalemate = self.test_move_game_won(row, column, self.get_valid_moves(
                                    row, column))
                                # if there are some valid moves that don't put black general in check.
                                if is_checkmate_or_stalemate is False:
                                    return True
                                else:
                                    continue
                    # if after the loop and is_checkmate is True then it means there are no moves that black can do
                    # that will not put the black general in check, meaning checkmate or stalemate.
                if is_checkmate_or_stalemate is True:
                    self._game_state = "RED_WON"
                    return True
            elif move_from_game_piece.get_game_piece_color() == "black":
                is_checkmate_or_stalemate = None
                # test all the moves that the red pieces have
                for row in range(0, 10):
                    for column in range(0, 9):
                        if self._game_board.get_board_point(row, column).is_occupied() is True:
                            if self._game_board.get_board_point(row, column).get_piece_on_point().\
                                    get_game_piece_color() == "red":
                                # test that piece's moves to see if after they do the move, is the red general in
                                # check using test_move_game_won method.
                                is_checkmate_or_stalemate = self.test_move_game_won(row, column, self.get_valid_moves(
                                    row, column))
                                if is_checkmate_or_stalemate is False:
                                    # means there are some valid moves that don't put red general in check.
                                    return True
                                else:
                                    continue
                    # if after the loop and is_checkmate is True then it means there are no moves that red can do
                    # that will not put the red general in check, meaning checkmate or stalemate.
                if is_checkmate_or_stalemate is True:
                    self._game_state = "BLACK_WON"
                    return True
        # if the move is not in the valid moves list.
        else:
            return False

    def get_valid_moves(self, row_move_from_index, column_move_from_index):
        """Takes two parameters a row index moving from, a column index moving from, returns a list of valid moves.
        Note: does not check for if the move will cause a check."""
        valid_moves = []

        # if the move from or move to is out of range.
        if row_move_from_index not in range(0, 10):
            return False
        # if the move from or move to is out of range.
        elif column_move_from_index not in range(0, 9):
            return False

        # if there is no piece to get valid moves from.
        if self._game_board.get_board_point(row_move_from_index, column_move_from_index).is_occupied() is False:
            return False

        move_from_game_piece = self._game_board.get_board_point(row_move_from_index, column_move_from_index).\
            get_piece_on_point()

        # if the game piece is a general or advisor.
        if isinstance(move_from_game_piece, General) or isinstance(move_from_game_piece, Advisor):
            # get the list of possible moves from the piece's possible moves method.
            list_of_possible_moves = move_from_game_piece.possible_moves()

            for coordinates in list_of_possible_moves:
                # if the space is not occupied.
                if self._game_board.get_board_point(coordinates[0], coordinates[1]).is_occupied() is False:
                    # add the coordinates to the valid moves list.
                    valid_moves.append(coordinates)
                # if the space is occupied.
                else:
                    # if the piece color on the point is the saame as the piece moving.
                    if self._game_board.get_board_point(coordinates[0], coordinates[1]).get_piece_on_point().\
                            get_game_piece_color() == move_from_game_piece.get_game_piece_color():
                        continue
                    else:
                        # add the coordinates to the valid moves list.
                        valid_moves.append(coordinates)

            # test if the valid moves list will cause general seeing general.
            valid_moves = self.will_general_see_general(row_move_from_index, column_move_from_index, valid_moves)

            return valid_moves

        # if the game piece is an elephant piece.
        if isinstance(move_from_game_piece, Elephant):
            # get the list of possible moves from the piece's possible moves method.
            list_of_possible_moves = move_from_game_piece.possible_moves()

            # first check all four diagonal points away from the current position.
            for row_number in range(-1, 2):
                for column_number in range(-1, 2):
                    if row_number == 0 or column_number == 0:
                        continue
                    else:
                        adjacent_row = row_move_from_index + row_number
                        adjacent_column = column_move_from_index + column_number

                        # check if the adjacent diagonal position is occupied.
                        if adjacent_row in range(0, 10) and adjacent_column in range(0, 9):
                            # if the adjacent diagonal position is occupied.
                            if self._game_board.get_board_point(adjacent_row, adjacent_column).is_occupied() is True:
                                # get the next diagonal point from the occupied point
                                adjacent_row = adjacent_row + row_number
                                adjacent_column = adjacent_column + column_number
                                if (adjacent_row, adjacent_column) in list_of_possible_moves:
                                    # remove the points that are blocked in the list_of_possible_moves
                                    list_of_possible_moves.remove((adjacent_row, adjacent_column))
                            else:
                                continue
                        else:
                            continue

            # now check if the actual move to points is occupied.
            for coordinates in list_of_possible_moves:
                # if the space is not occupied.
                if self._game_board.get_board_point(coordinates[0], coordinates[1]).is_occupied() is False:
                    valid_moves.append(coordinates)
                # if the space is occupied.
                else:
                    # if the piece color on the space is the same as the piece that is doing the move.
                    if self._game_board.get_board_point(coordinates[0], coordinates[1]).get_piece_on_point().\
                            get_game_piece_color() == move_from_game_piece.get_game_piece_color():
                        continue
                    else:
                        # add the space to the valid moves list.
                        valid_moves.append(coordinates)

            # test if the moves in the valid moves list will cause general seeing general.
            valid_moves = self.will_general_see_general(row_move_from_index, column_move_from_index, valid_moves)

            return valid_moves

        # if the game piece is a horse piece.
        if isinstance(move_from_game_piece, Horse):
            # get the list of possible moves from the piece's possible moves method.
            list_of_possible_moves = move_from_game_piece.possible_moves()

            # check if the point on the right is blocking
            column_number = 1
            adjacent_column = column_move_from_index + column_number
            if adjacent_column in range(0, 9):
                if self._game_board.get_board_point(row_move_from_index, adjacent_column).is_occupied() is True:
                    # the move that is blocked
                    adjacent_row = row_move_from_index + 1
                    adjacent_column = adjacent_column + column_number
                    if (adjacent_row, adjacent_column) in list_of_possible_moves:
                        list_of_possible_moves.remove((adjacent_row, adjacent_column))
                    # the move that is blocked
                    adjacent_row = row_move_from_index - 1
                    if (adjacent_row, adjacent_column) in list_of_possible_moves:
                        list_of_possible_moves.remove((adjacent_row, adjacent_column))

            # check if the point on the left is blocking
            column_number = -1
            adjacent_column = column_move_from_index + column_number
            if adjacent_column in range(0, 9):
                if self._game_board.get_board_point(row_move_from_index, adjacent_column).is_occupied() is True:
                    # the move that is blocked
                    adjacent_row = row_move_from_index + 1
                    adjacent_column = adjacent_column + column_number
                    if (adjacent_row, adjacent_column) in list_of_possible_moves:
                        list_of_possible_moves.remove((adjacent_row, adjacent_column))
                    # the move that is blocked
                    adjacent_row = row_move_from_index - 1
                    if (adjacent_row, adjacent_column) in list_of_possible_moves:
                        list_of_possible_moves.remove((adjacent_row, adjacent_column))

            # check if the point on top is blocking
            row_number = -1
            adjacent_row = row_move_from_index + row_number
            if adjacent_row in range(0, 10):
                if self._game_board.get_board_point(adjacent_row, column_move_from_index).is_occupied() is True:
                    # the move that is blocked
                    adjacent_row = adjacent_row + row_number
                    adjacent_column = column_move_from_index + 1
                    if (adjacent_row, adjacent_column) in list_of_possible_moves:
                        list_of_possible_moves.remove((adjacent_row, adjacent_column))
                    # the move that is blocked
                    adjacent_column = column_move_from_index - 1
                    if (adjacent_row, adjacent_column) in list_of_possible_moves:
                        list_of_possible_moves.remove((adjacent_row, adjacent_column))

            # check if the point on the bottom is blocking
            row_number = 1
            adjacent_row = row_move_from_index + row_number
            if adjacent_row in range(0, 10):
                if self._game_board.get_board_point(adjacent_row, column_move_from_index).is_occupied() is True:
                    # the move that is blocked
                    adjacent_row = adjacent_row + row_number
                    adjacent_column = column_move_from_index + 1
                    if (adjacent_row, adjacent_column) in list_of_possible_moves:
                        list_of_possible_moves.remove((adjacent_row, adjacent_column))
                    # the move that is blocked
                    adjacent_column = column_move_from_index - 1
                    if (adjacent_row, adjacent_column) in list_of_possible_moves:
                        list_of_possible_moves.remove((adjacent_row, adjacent_column))

            # now check if the actual move to points is occupied.
            for coordinates in list_of_possible_moves:
                # if the space is not occupied.
                if self._game_board.get_board_point(coordinates[0], coordinates[1]).is_occupied() is False:
                    # add coordinates to the valid moves list.
                    valid_moves.append(coordinates)
                # if the space is occupied
                else:
                    # if the piece color on the space is the same as the piece that is doing the move.
                    if self._game_board.get_board_point(coordinates[0], coordinates[1]).get_piece_on_point().\
                            get_game_piece_color() == move_from_game_piece.get_game_piece_color():
                        continue
                    else:
                        # add coordinates to the valid moves list.
                        valid_moves.append(coordinates)

            # test if the moves in the valid moves list will cause general seeing general.
            valid_moves = self.will_general_see_general(row_move_from_index, column_move_from_index, valid_moves)

            return valid_moves

        if isinstance(move_from_game_piece, Chariot):

            # all possible moves up
            adjacent_row_up = row_move_from_index - 1
            while adjacent_row_up >= 0:
                # if the space is not occupied.
                if self._game_board.get_board_point(adjacent_row_up, column_move_from_index).is_occupied() is False:
                    # add the space to the valid moves list.
                    valid_moves.append((adjacent_row_up, column_move_from_index))
                    adjacent_row_up -= 1
                else:
                    # if the space has a piece that is the same color as the piece moving.
                    if self._game_board.get_board_point(adjacent_row_up, column_move_from_index).get_piece_on_point().\
                            get_game_piece_color() == move_from_game_piece.get_game_piece_color():
                        break
                    else:
                        # add the space to the valid moves list.
                        valid_moves.append((adjacent_row_up, column_move_from_index))
                        break

            # all possible moves down
            adjacent_row_down = row_move_from_index + 1
            while adjacent_row_down <= 9:
                # if the space is not occupied.
                if self._game_board.get_board_point(adjacent_row_down, column_move_from_index).is_occupied() is False:
                    # add the space to the valid moves list.
                    valid_moves.append((adjacent_row_down, column_move_from_index))
                    adjacent_row_down += 1
                else:
                    # if the space has a piece that is the same color as the piece moving.
                    if self._game_board.get_board_point(adjacent_row_down, column_move_from_index).\
                            get_piece_on_point().get_game_piece_color() == move_from_game_piece.get_game_piece_color():
                        break
                    else:
                        # add the space to the valid moves list.
                        valid_moves.append((adjacent_row_down, column_move_from_index))
                        break

            # all possible moves left
            adjacent_column_left = column_move_from_index - 1
            while adjacent_column_left >= 0:
                # if the space is not occupied.
                if self._game_board.get_board_point(row_move_from_index, adjacent_column_left).is_occupied() is False:
                    # add the space to the valid moves list.
                    valid_moves.append((row_move_from_index, adjacent_column_left))
                    adjacent_column_left -= 1
                else:
                    # if the space has a piece that is the same color as the piece moving.
                    if self._game_board.get_board_point(row_move_from_index, adjacent_column_left).\
                            get_piece_on_point().get_game_piece_color() == move_from_game_piece.get_game_piece_color():
                        break
                    else:
                        # add the space to the valid moves list.
                        valid_moves.append((row_move_from_index, adjacent_column_left))
                        break

            # all possible moves right
            adjacent_column_right = column_move_from_index + 1
            while adjacent_column_right <= 8:
                # if the space is not occupied.
                if self._game_board.get_board_point(row_move_from_index, adjacent_column_right).is_occupied() is False:
                    # add the space to the valid moves list.
                    valid_moves.append((row_move_from_index, adjacent_column_right))
                    adjacent_column_right += 1
                else:
                    # if the space has a piece that is the same color as the piece moving.
                    if self._game_board.get_board_point(row_move_from_index, adjacent_column_right).\
                            get_piece_on_point().get_game_piece_color() == move_from_game_piece.get_game_piece_color():
                        break
                    else:
                        # add the space to the valid moves list.
                        valid_moves.append((row_move_from_index, adjacent_column_right))
                        break

            # test if the moves in the valid moves list will cause general seeing general.
            valid_moves = self.will_general_see_general(row_move_from_index, column_move_from_index, valid_moves)

            return valid_moves

        # if the piece is a cannon piece.
        if isinstance(move_from_game_piece, Cannon):

            # use similar mechanics as chariot but if it hits a piece, keep looking until the next is an enemy or
            # friend or end of board.

            # all possible moves up
            adjacent_row_up = row_move_from_index - 1
            found_piece = 0
            while adjacent_row_up >= 0 and found_piece < 2:
                # if space is not occupied
                if self._game_board.get_board_point(adjacent_row_up, column_move_from_index).is_occupied() is False:
                    if found_piece < 1:
                        # add the space to the valid moves list.
                        valid_moves.append((adjacent_row_up, column_move_from_index))
                        adjacent_row_up -= 1
                    else:
                        adjacent_row_up -= 1
                else:
                    # if the space is occupied
                    found_piece += 1
                    if found_piece == 2:
                        # if the space is occupied by a friend.
                        if self._game_board.get_board_point(adjacent_row_up, column_move_from_index). \
                                get_piece_on_point().get_game_piece_color() == move_from_game_piece. \
                                get_game_piece_color():
                            break
                        else:
                            # if the next piece is an enemy, add that space to valid moves
                            valid_moves.append((adjacent_row_up, column_move_from_index))
                            break
                    else:
                        # keep looking at the spaces up
                        adjacent_row_up -= 1

            # all possible moves down
            adjacent_row_down = row_move_from_index + 1
            found_piece = 0
            while adjacent_row_down <= 9 and found_piece < 2:
                # if space is not occupied
                if self._game_board.get_board_point(adjacent_row_down, column_move_from_index).is_occupied() is False:
                    if found_piece < 1:
                        # add the space to the valid moves list.
                        valid_moves.append((adjacent_row_down, column_move_from_index))
                        adjacent_row_down += 1
                    else:
                        adjacent_row_down += 1
                else:
                    # if the space is occupied.
                    found_piece += 1
                    if found_piece == 2:
                        # if the space is occupied by a friend.
                        if self._game_board.get_board_point(adjacent_row_down, column_move_from_index). \
                                get_piece_on_point().get_game_piece_color() == move_from_game_piece. \
                                get_game_piece_color():
                            break
                        else:
                            # if the next piece is an enemy, add that space to valid moves
                            valid_moves.append((adjacent_row_down, column_move_from_index))
                            break
                    else:
                        # keep looking at the spaces down
                        adjacent_row_down += 1

            # all possible moves left
            adjacent_column_left = column_move_from_index - 1
            found_piece = 0
            while adjacent_column_left >= 0 and found_piece < 2:
                # if space is not occupied
                if self._game_board.get_board_point(row_move_from_index, adjacent_column_left).is_occupied() is False:
                    if found_piece < 1:
                        # add the space to the valid moves list.
                        valid_moves.append((row_move_from_index, adjacent_column_left))
                        adjacent_column_left -= 1
                    else:
                        adjacent_column_left -= 1
                else:
                    found_piece += 1
                    if found_piece == 2:
                        # if the space is occupied by a friend.
                        if self._game_board.get_board_point(row_move_from_index, adjacent_column_left). \
                                get_piece_on_point().get_game_piece_color() == move_from_game_piece. \
                                get_game_piece_color():
                            break
                        else:
                            # if the next piece is an enemy, add that space to valid moves
                            valid_moves.append((row_move_from_index, adjacent_column_left))
                            break
                    # keep looking at spaces left
                    else:
                        adjacent_column_left -= 1

            # all possible moves right
            adjacent_column_right = column_move_from_index + 1
            found_piece = 0
            while adjacent_column_right <= 8 and found_piece < 2:
                # if space is not occupied.
                if self._game_board.get_board_point(row_move_from_index, adjacent_column_right).is_occupied() is False:
                    if found_piece < 1:
                        # add the space to the valid moves list.
                        valid_moves.append((row_move_from_index, adjacent_column_right))
                        adjacent_column_right += 1
                    else:
                        adjacent_column_right += 1
                # if the space is occupied.
                else:
                    found_piece += 1
                    if found_piece == 2:
                        # if the space is occupied by a friend.
                        if self._game_board.get_board_point(row_move_from_index, adjacent_column_right). \
                                get_piece_on_point().get_game_piece_color() == move_from_game_piece. \
                                get_game_piece_color():
                            break
                        else:
                            # if the next piece is an enemy, add that space to valid moves
                            valid_moves.append((row_move_from_index, adjacent_column_right))
                            break
                    # keep looking at the spaces right
                    else:
                        adjacent_column_right += 1

            # test if the moves in the valid moves list will cause general seeing general.
            valid_moves = self.will_general_see_general(row_move_from_index, column_move_from_index, valid_moves)

            return valid_moves

        # if the piece is a soldier piece
        if isinstance(move_from_game_piece, Soldier):

            # if the piece that is moving is red
            if move_from_game_piece.get_game_piece_color() == "red":

                # valid move down
                adjacent_row_down = row_move_from_index + 1
                if adjacent_row_down in range(0, 10):
                    # if the space is not occupied
                    if self._game_board.get_board_point(adjacent_row_down, column_move_from_index). \
                            is_occupied() is False:
                        # add the space to the valid moves list.
                        valid_moves.append((adjacent_row_down, column_move_from_index))
                    # if the space is occupied
                    else:
                        # if the space is an enemy.
                        if self._game_board.get_board_point(adjacent_row_down, column_move_from_index). \
                                get_piece_on_point().get_game_piece_color() != move_from_game_piece. \
                                get_game_piece_color():
                            # add the space to the valid moves list.
                            valid_moves.append((adjacent_row_down, column_move_from_index))

                # after the piece crosses the river.
                if row_move_from_index > 4:
                    # valid move left
                    adjacent_column_left = column_move_from_index - 1
                    if adjacent_column_left in range(0, 9):
                        # if the space is not occupied
                        if self._game_board.get_board_point(row_move_from_index, adjacent_column_left). \
                                is_occupied() is False:
                            # add the space to the valid moves list.
                            valid_moves.append((row_move_from_index, adjacent_column_left))
                        # if the space is occupied
                        else:
                            # if the space is an enemy.
                            if self._game_board.get_board_point(row_move_from_index, adjacent_column_left). \
                                    get_piece_on_point().get_game_piece_color() != move_from_game_piece. \
                                    get_game_piece_color():
                                # add the space to the valid moves list.
                                valid_moves.append((row_move_from_index, adjacent_column_left))

                    # valid more right
                    adjacent_column_right = column_move_from_index + 1
                    if adjacent_column_right in range(0, 9):
                        # if the space is not occupied
                        if self._game_board.get_board_point(row_move_from_index, adjacent_column_right). \
                                is_occupied() is False:
                            # add the space to the valid moves list.
                            valid_moves.append((row_move_from_index, adjacent_column_right))
                        # if the space is occupied
                        else:
                            # if the space is an enemy.
                            if self._game_board.get_board_point(row_move_from_index, adjacent_column_right). \
                                    get_piece_on_point().get_game_piece_color() != move_from_game_piece. \
                                    get_game_piece_color():
                                # add the space to the valid moves list.
                                valid_moves.append((row_move_from_index, adjacent_column_right))

            # if the piece that is moving is black
            if move_from_game_piece.get_game_piece_color() == "black":

                # valid move up
                adjacent_row_up = row_move_from_index - 1
                if adjacent_row_up in range(0, 10):
                    # if the space is not occupied
                    if self._game_board.get_board_point(adjacent_row_up, column_move_from_index). \
                            is_occupied() is False:
                        # add the space to the valid moves list.
                        valid_moves.append((adjacent_row_up, column_move_from_index))
                    # if the space is occupied
                    else:
                        # if the space is an enemy.
                        if self._game_board.get_board_point(adjacent_row_up, column_move_from_index). \
                                get_piece_on_point().get_game_piece_color() != move_from_game_piece. \
                                get_game_piece_color():
                            # add the space to the valid moves list.
                            valid_moves.append((adjacent_row_up, column_move_from_index))

                # once the black piece crosses the river
                if row_move_from_index < 5:

                    # valid move left
                    adjacent_column_left = column_move_from_index - 1
                    if adjacent_column_left in range(0, 9):
                        # if the space is not occupied
                        if self._game_board.get_board_point(row_move_from_index, adjacent_column_left). \
                                is_occupied() is False:
                            # add the space to the valid moves list.
                            valid_moves.append((row_move_from_index, adjacent_column_left))
                        # if the space is occupied
                        else:
                            # if the space is an enemy.
                            if self._game_board.get_board_point(row_move_from_index, adjacent_column_left). \
                                    get_piece_on_point().get_game_piece_color() != move_from_game_piece. \
                                    get_game_piece_color():
                                # add the space to the valid moves list.
                                valid_moves.append((row_move_from_index, adjacent_column_left))

                    # valid more right
                    adjacent_column_right = column_move_from_index + 1
                    if adjacent_column_right in range(0, 9):
                        # if the space is not occupied
                        if self._game_board.get_board_point(row_move_from_index, adjacent_column_right). \
                                is_occupied() is False:
                            # add the space to the valid moves list.
                            valid_moves.append((row_move_from_index, adjacent_column_right))
                        # if the space is occupied
                        else:
                            # if the space is an enemy.
                            if self._game_board.get_board_point(row_move_from_index, adjacent_column_right). \
                                    get_piece_on_point().get_game_piece_color() != move_from_game_piece. \
                                    get_game_piece_color():
                                # add the space to the valid moves list.
                                valid_moves.append((row_move_from_index, adjacent_column_right))

            # test if the moves in the valid moves list will cause general seeing general.
            valid_moves = self.will_general_see_general(row_move_from_index, column_move_from_index, valid_moves)

            return valid_moves

    def will_general_see_general(self, piece_current_row, piece_current_column, list_of_possible_moves):
        """Takes a game piece's current row on the board, current column on the board, and a list of moves to test."""
        red_gen_location = self._game_board.get_red_general_location()
        black_gen_location = self._game_board.get_black_general_location()
        piece_count = 0
        # create a separate list so we can iterate and remove things from list_of_possible_moves if necessary.
        valid_list = list(list_of_possible_moves)

        if self._game_board.get_board_point(piece_current_row, piece_current_column).get_piece_on_point(). \
                get_piece_type() != "general":
            # if the generals are on the same column.
            if red_gen_location[1] == black_gen_location[1]:
                # if the piece is on the same column as the generals.
                if piece_current_column == black_gen_location[1]:
                    # look at all the spaces between the generals.
                    for row in range(red_gen_location[0]+1, black_gen_location[0]):
                        # count the number of pieces between the generals
                        if self._game_board.get_board_point(row, black_gen_location[1]).is_occupied() is True:
                            piece_count += 1
                    if piece_count > 1:
                        return list_of_possible_moves
                    # if there is only one piece
                    elif piece_count == 1:
                        # find the coordinates that are not on the same row as the generals
                        for coordinates in valid_list:
                            if coordinates[1] != black_gen_location[1]:
                                # remove that coordinate from the list of possible moves.
                                list_of_possible_moves.remove(coordinates)
                        return list_of_possible_moves

        if self._game_board.get_board_point(piece_current_row, piece_current_column).get_piece_on_point().\
                get_piece_type() == "general":
            # if the piece doing the moving is red.
            if self._game_board.get_board_point(piece_current_row, piece_current_column).get_piece_on_point().\
                    get_game_piece_color() == "red":
                # if the generals columns are different
                if piece_current_column != black_gen_location[1]:
                    # iterate from the black general to row 0.
                    for row in range(black_gen_location[0] - 1, -1, -1):
                        if self._game_board.get_board_point(row, black_gen_location[1]).is_occupied() is True:
                            piece_count += 1
                            # if there is one piece and it is at row in front of red general.
                            if piece_count == 1 and row == piece_current_row + 1:
                                for coordinates in valid_list:
                                    if coordinates[0] == row and coordinates[1] == black_gen_location[1]:
                                        # remove those coordinate from the list of possible moves.
                                        list_of_possible_moves.remove(coordinates)
                                return list_of_possible_moves
                            # if there is one piece and it is at the same row as the red general.
                            elif piece_count == 1 and row == piece_current_row:
                                for coordinates in valid_list:
                                    if coordinates[0] >= row and coordinates[1] == black_gen_location[1]:
                                        # remove those coordinate from the list of possible moves.
                                        list_of_possible_moves.remove(coordinates)
                                return list_of_possible_moves
                            elif piece_count == 1 and row < piece_current_row:
                                for coordinates in valid_list:
                                    if coordinates[1] == black_gen_location[1]:
                                        # remove those coordinate from the list of possible moves.
                                        list_of_possible_moves.remove(coordinates)
                                return list_of_possible_moves
                            else:
                                continue
                        else:
                            continue
                    # if there are no other pieces
                    if piece_count == 0:
                        for coordinates in valid_list:
                            if coordinates[1] == black_gen_location[1]:
                                # remove those coordinate from the list of possible moves.
                                list_of_possible_moves.remove(coordinates)

                # if the generals are on the same column
                elif piece_current_column == black_gen_location[1]:
                    # look at the rows between the generals, starting from the black.
                    for row in range(black_gen_location[0] - 1, red_gen_location[0], -1):
                        # if the space is occupied.
                        if self._game_board.get_board_point(row, red_gen_location[1]).is_occupied() is True:
                            piece_count += 1
                            # if the generals are on the same column if there is only one piece and it is in front
                            # of the red general.
                            if piece_count == 1 and row == piece_current_row + 1:
                                for coordinates in valid_list:
                                    if coordinates[0] <= row and coordinates[1] == black_gen_location[1]:
                                        # remove those coordinate from the list of possible moves.
                                        list_of_possible_moves.remove(coordinates)
                            else:
                                continue
                        else:
                            continue
            # if the piece moving is black
            elif self._game_board.get_board_point(piece_current_row, piece_current_column).get_piece_on_point().\
                    get_game_piece_color() == "black":
                # if the generals columns are different.
                if piece_current_column != red_gen_location[1]:
                    # look at the rows from between the red gen to the end of the board.
                    for row in range(red_gen_location[0]+1, 10):
                        if self._game_board.get_board_point(row, red_gen_location[1]).is_occupied() is True:
                            piece_count += 1
                            # if there a piece and it is on the row above the black general.
                            if piece_count == 1 and row == piece_current_row - 1:
                                for coordinates in valid_list:
                                    if coordinates[0] == row and coordinates[1] == red_gen_location[1]:
                                        # remove those coordinate from the list of possible moves.
                                        list_of_possible_moves.remove(coordinates)
                                return list_of_possible_moves
                            # if there is a piece and it is on the same row as the general.
                            elif piece_count == 1 and row == piece_current_row:
                                for coordinates in valid_list:
                                    if coordinates[0] <= row and coordinates[1] == red_gen_location[1]:
                                        # remove those coordinate from the list of possible moves.
                                        list_of_possible_moves.remove(coordinates)
                                return list_of_possible_moves
                            # if there is a piece and it on the row below the black general.
                            elif piece_count == 1 and row == piece_current_row + 1:
                                for coordinates in valid_list:
                                    if coordinates[1] == red_gen_location[1]:
                                        # remove those coordinate from the list of possible moves.
                                        list_of_possible_moves.remove(coordinates)
                                return list_of_possible_moves
                            else:
                                continue
                        else:
                            continue
                    # if there are no other pieces.
                    if piece_count == 0:
                        for coordinates in valid_list:
                            if coordinates[1] == red_gen_location[1]:
                                # remove those coordinate from the list of possible moves.
                                list_of_possible_moves.remove(coordinates)
                # if the generals are on the same column.
                elif piece_current_column == red_gen_location[1]:
                    for row in range(red_gen_location[0]+1, black_gen_location[0]):
                        if self._game_board.get_board_point(row, red_gen_location[1]).is_occupied() is True:
                            piece_count += 1
                            # if the generals are on the same column if there is only one piece and it is in front
                            # of the black general.
                            if piece_count == 1 and piece_current_row == row + 1:
                                for coordinates in valid_list:
                                    if coordinates[0] <= row and coordinates[1] == red_gen_location[1]:
                                        # remove those coordinate from the list of possible moves.
                                        list_of_possible_moves.remove(coordinates)

        return list_of_possible_moves

    def test_move_in_check(self, test_piece_row, test_piece_column, list_of_moves):
        """Takes the piece's current row, current column, and a list of moves and performs the move then checks if their
         own teams general will be in check after doing the move, if it is then remove that move from the list of valid
         moves and returns the list."""
        # create a new list identical to the list of moves so we can iterate through the list and remove coordinates
        # from the list of moves if necessary.
        valid_moves = list(list_of_moves)
        move_from_game_piece = self._game_board.get_board_point(test_piece_row, test_piece_column). \
            get_piece_on_point()

        if move_from_game_piece.get_game_piece_color() == "black":
            for coordinates in valid_moves:
                # if the coordinates is already occupied.
                save_piece = self._game_board.get_board_point(coordinates[0], coordinates[1]).get_piece_on_point()
                save_occupy_status = self._game_board.get_board_point(coordinates[0], coordinates[1]).is_occupied()
                # move game piece to new position
                self._game_board.get_board_point(coordinates[0], coordinates[1]).\
                    set_piece_on_point(move_from_game_piece)
                # update the game piece location to the new position
                self._game_board.get_board_point(coordinates[0], coordinates[1]).get_piece_on_point().\
                    set_location(coordinates[0], coordinates[1])
                # change occupy status of new position.
                self._game_board.get_board_point(coordinates[0], coordinates[1]).set_occupied(True)
                # remove game piece from old position
                self._game_board.get_board_point(test_piece_row, test_piece_column).\
                    remove_piece_on_point(test_piece_row, test_piece_column)
                # change occupy status for old position to False
                self._game_board.get_board_point(test_piece_row, test_piece_column).set_occupied(False)

                black_general_location = self._game_board.get_black_general_location()
                black_general_in_check = False
                # look at all the valid moves of the red pieces
                for row in range(0, 10):
                    for column in range(0, 9):
                        if self._game_board.get_board_point(row, column).is_occupied() is True:
                            if self._game_board.get_board_point(row, column).get_piece_on_point(). \
                                    get_game_piece_color() == "red":
                                # if the black general's location is in any of those valid moves.
                                if black_general_location in self.get_valid_moves(row, column):
                                    black_general_in_check = True
                                else:
                                    continue
                            else:
                                continue
                        else:
                            continue

                if black_general_in_check is True:
                    # reverse the move
                    # move game piece back to old position
                    self._game_board.get_board_point(test_piece_row, test_piece_column).\
                        set_piece_on_point(self._game_board.get_board_point(coordinates[0], coordinates[1]).
                                           get_piece_on_point())
                    # update the game piece location.
                    self._game_board.get_board_point(test_piece_row, test_piece_column).get_piece_on_point().\
                        set_location(test_piece_row, test_piece_column)
                    # change the occupy status
                    self._game_board.get_board_point(test_piece_row, test_piece_column).set_occupied(True)
                    # remove the game piece from "new" location and set back to what it was
                    self._game_board.get_board_point(coordinates[0], coordinates[1]).set_piece_on_point(save_piece)
                    self._game_board.get_board_point(coordinates[0], coordinates[1]).set_occupied(save_occupy_status)

                    # remove the coordinates from the list of moves.
                    list_of_moves.remove(coordinates)
                else:
                    # reverse the move
                    # move game piece back to old position
                    self._game_board.get_board_point(test_piece_row, test_piece_column).\
                        set_piece_on_point(self._game_board.get_board_point(coordinates[0], coordinates[1]).
                                           get_piece_on_point())
                    # update the game piece location.
                    self._game_board.get_board_point(test_piece_row, test_piece_column).get_piece_on_point().\
                        set_location(test_piece_row, test_piece_column)
                    # change the occupy status
                    self._game_board.get_board_point(test_piece_row, test_piece_column).set_occupied(True)
                    # remove the game piece from "new" location and set back to what it was
                    self._game_board.get_board_point(coordinates[0], coordinates[1]).set_piece_on_point(save_piece)
                    self._game_board.get_board_point(coordinates[0], coordinates[1]).set_occupied(save_occupy_status)
            return list_of_moves

        if move_from_game_piece.get_game_piece_color() == "red":
            for coordinates in valid_moves:
                # if the coordinates is already occupied.
                save_piece = self._game_board.get_board_point(coordinates[0], coordinates[1]).get_piece_on_point()
                save_occupy_status = self._game_board.get_board_point(coordinates[0], coordinates[1]).is_occupied()
                # move game piece to new position
                self._game_board.get_board_point(coordinates[0], coordinates[1]).\
                    set_piece_on_point(move_from_game_piece)
                # update the game piece location to the new position
                self._game_board.get_board_point(coordinates[0], coordinates[1]).get_piece_on_point().\
                    set_location(coordinates[0], coordinates[1])
                # change occupy status of new position.
                self._game_board.get_board_point(coordinates[0], coordinates[1]).set_occupied(True)
                # remove game piece from old position
                self._game_board.get_board_point(test_piece_row, test_piece_column).\
                    remove_piece_on_point(test_piece_row, test_piece_column)
                # change occupy status for old position to False
                self._game_board.get_board_point(test_piece_row, test_piece_column).set_occupied(False)

                red_general_location = self._game_board.get_red_general_location()
                red_general_in_check = False
                # look at all the valid moves of the red pieces
                for row in range(0, 10):
                    for column in range(0, 9):
                        if self._game_board.get_board_point(row, column).is_occupied() is True:
                            if self._game_board.get_board_point(row, column).get_piece_on_point(). \
                                    get_game_piece_color() == "black":
                                # if the black general's location is in any of those valid moves.
                                if red_general_location in self.get_valid_moves(row, column):
                                    red_general_in_check = True
                                else:
                                    continue
                            else:
                                continue
                        else:
                            continue

                if red_general_in_check is True:
                    # reverse the move
                    # move game piece back to old position
                    self._game_board.get_board_point(test_piece_row, test_piece_column).\
                        set_piece_on_point(self._game_board.get_board_point(coordinates[0], coordinates[1]).
                                           get_piece_on_point())
                    # update the game piece location.
                    self._game_board.get_board_point(test_piece_row, test_piece_column).get_piece_on_point().\
                        set_location(test_piece_row, test_piece_column)
                    # change the occupy status
                    self._game_board.get_board_point(test_piece_row, test_piece_column).set_occupied(True)
                    # remove the game piece from old location and set back to what it was
                    self._game_board.get_board_point(coordinates[0], coordinates[1]).set_piece_on_point(save_piece)
                    self._game_board.get_board_point(coordinates[0], coordinates[1]).set_occupied(save_occupy_status)

                    # remove the coordinates from the list of moves.
                    list_of_moves.remove(coordinates)
                else:
                    # reverse the move
                    # move game piece back to old position
                    self._game_board.get_board_point(test_piece_row, test_piece_column).\
                        set_piece_on_point(self._game_board.get_board_point(coordinates[0], coordinates[1]).
                                           get_piece_on_point())
                    # update the game piece location.
                    self._game_board.get_board_point(test_piece_row, test_piece_column).get_piece_on_point().\
                        set_location(test_piece_row, test_piece_column)
                    # change the occupy status
                    self._game_board.get_board_point(test_piece_row, test_piece_column).set_occupied(True)
                    # remove the game piece from old location and set back to what it was
                    self._game_board.get_board_point(coordinates[0], coordinates[1]).set_piece_on_point(save_piece)
                    self._game_board.get_board_point(coordinates[0], coordinates[1]).set_occupied(save_occupy_status)
            return list_of_moves
        # if color is not red or black
        return list_of_moves

    def is_in_check(self, color):
        """Takes a color: either "red" or "black" and returns True if that color's general is in check. Otherwise,
        returns False."""

        if color.lower() == "red":
            red_general_location = self._game_board.get_red_general_location()
            # look at all the valid moves of the black pieces
            for row in range(0, 10):
                for column in range(0, 9):
                    if self._game_board.get_board_point(row, column).is_occupied() is True:
                        if self._game_board.get_board_point(row, column).get_piece_on_point().\
                                get_game_piece_color() == "black":
                            # if the coordinates of the red general is in one of the moves.
                            if red_general_location in self.get_valid_moves(row, column):
                                return True
            return False

        if color.lower() == "black":
            black_general_location = self._game_board.get_black_general_location()
            # look at all the valid moves of the red pieces
            for row in range(0, 10):
                for column in range(0, 9):
                    if self._game_board.get_board_point(row, column).is_occupied() is True:
                        if self._game_board.get_board_point(row, column).get_piece_on_point().\
                                get_game_piece_color() == "red":
                            # if the black general's location is in any of those valid moves.
                            if black_general_location in self.get_valid_moves(row, column):
                                return True
            return False

    def test_move_game_won(self, test_piece_row, test_piece_column, list_of_moves):
        """Takes a piece's current row, current column, and their list of moves. Tests to see if the their team's
        general will be in check after the moves. Returns false if one of the moves makes the general not in check,
        otherwise, returns True."""
        # create a new list identical to the list of moves so we can iterate through the list.
        valid_moves = list(list_of_moves)
        move_from_game_piece = self._game_board.get_board_point(test_piece_row, test_piece_column). \
            get_piece_on_point()

        if move_from_game_piece.get_game_piece_color() == "black":
            black_general_in_check = True

            for coordinates in valid_moves:
                # if the coordinates is already occupied or not. change this !!!!
                save_piece = self._game_board.get_board_point(coordinates[0], coordinates[1]).get_piece_on_point()
                save_occupy_status = self._game_board.get_board_point(coordinates[0], coordinates[1]).is_occupied()
                # move game piece to new position
                self._game_board.get_board_point(coordinates[0], coordinates[1]).\
                    set_piece_on_point(move_from_game_piece)
                # update the game piece location to the new position
                self._game_board.get_board_point(coordinates[0], coordinates[1]).get_piece_on_point().\
                    set_location(coordinates[0], coordinates[1])
                # change occupy status of new position.
                self._game_board.get_board_point(coordinates[0], coordinates[1]).set_occupied(True)
                # remove game piece from old position
                self._game_board.get_board_point(test_piece_row, test_piece_column).\
                    remove_piece_on_point(test_piece_row, test_piece_column)
                # change occupy status for old position to False
                self._game_board.get_board_point(test_piece_row, test_piece_column).set_occupied(False)

                # is black still in check after the move?
                if self.is_in_check("black") is False:
                    black_general_in_check = False

                self._game_board.get_board_point(test_piece_row, test_piece_column).\
                    set_piece_on_point(self._game_board.get_board_point(coordinates[0], coordinates[1]).
                                       get_piece_on_point())
                # update the game piece location.
                self._game_board.get_board_point(test_piece_row, test_piece_column).get_piece_on_point(). \
                    set_location(test_piece_row, test_piece_column)
                # change the occupy status
                self._game_board.get_board_point(test_piece_row, test_piece_column).set_occupied(True)
                # remove the game piece from old location and set back to what it was
                self._game_board.get_board_point(coordinates[0], coordinates[1]).set_piece_on_point(save_piece)
                self._game_board.get_board_point(coordinates[0], coordinates[1]).set_occupied(save_occupy_status)
                continue

            return black_general_in_check

        if move_from_game_piece.get_game_piece_color() == "red":
            red_general_in_check = True
            for coordinates in valid_moves:
                # if the coordinates is already occupied.
                save_piece = self._game_board.get_board_point(coordinates[0], coordinates[1]).get_piece_on_point()
                save_occupy_status = self._game_board.get_board_point(coordinates[0], coordinates[1]).is_occupied()
                # move game piece to new position
                self._game_board.get_board_point(coordinates[0], coordinates[1]).\
                    set_piece_on_point(move_from_game_piece)
                # update the game piece location to the new position
                self._game_board.get_board_point(coordinates[0], coordinates[1]).get_piece_on_point().\
                    set_location(coordinates[0], coordinates[1])
                # change occupy status of new position.
                self._game_board.get_board_point(coordinates[0], coordinates[1]).set_occupied(True)
                # remove game piece from old position
                self._game_board.get_board_point(test_piece_row, test_piece_column).\
                    remove_piece_on_point(test_piece_row, test_piece_column)
                # change occupy status for old position to False
                self._game_board.get_board_point(test_piece_row, test_piece_column).set_occupied(False)
                # is red is not in check after the move
                if self.is_in_check("red") is False:
                    red_general_in_check = False

                # reverse the move
                self._game_board.get_board_point(test_piece_row, test_piece_column).\
                    set_piece_on_point(self._game_board.get_board_point(coordinates[0], coordinates[1]).
                                       get_piece_on_point())
                # update the game piece location.
                self._game_board.get_board_point(test_piece_row, test_piece_column).get_piece_on_point(). \
                    set_location(test_piece_row, test_piece_column)
                # change the occupy status
                self._game_board.get_board_point(test_piece_row, test_piece_column).set_occupied(True)
                # remove the game piece from old location and set back to what it was
                self._game_board.get_board_point(coordinates[0], coordinates[1]).set_piece_on_point(save_piece)
                self._game_board.get_board_point(coordinates[0], coordinates[1]).set_occupied(save_occupy_status)
                continue

            return red_general_in_check

game = XiangqiGame()
print(game.make_move("B1", "C3"))
print(game.make_move("B8", "C8"))
print(game.make_move("C3", "E2"))
print(game.make_move("C8", "C4"))
print(game.make_move("B3", "C3"))
print(game.make_move("C4", "C1"))
print(game.make_move("E1", "D2"))
print(game.make_move("A10", "A9"))
print(game.make_move("E4", "E5"))
print(game.make_move("A9", "d9"))
print(game.make_move("D2", "E3"))
print(game.make_move("i10", "i9"))
print(game.make_move("E2", "G3"))
print(game.make_move("i9", "F9"))
print(game.make_move("E3", "E2"))
print(game.make_move("E7", "E6"))
print(game.make_move("A4","A5"))
print(game.make_move("D9", "D1"))
print(game.make_move("A5","A6"))
print(game.make_move("E6", "E5"))
print(game.make_move("A6","A7"))
print(game.make_move("E5", "E4"))
print(game.make_move("A7","A8"))
print(game.make_move("F9","F1"))
print(game.make_move("A8","A9"))
print(game.make_move("F1","G1"))
print(game.make_move("A9","A10"))
print(game.make_move("E10","D9"))
print(game.make_move("A10","B10"))
#print(game.make_move("E4","E3"))
print(game.make_move("D1","F1"))
print(game.make_move("A1","A10"))
print(game.make_move("D9","E9"))
print(game.make_move("A10","A1"))
print(game.make_move("E9","F9"))
print(game.make_move("A1","A10"))
#print(game.make_move("G1","G2"))
print(game.make_move("E4","E3"))
print(game.make_move("E2","D2"))
#print(game.make_move("G1","G2"))
print(game.make_move("F9","E9"))
print(game.make_move("A10","A1"))
print(game.make_move("G1","G2"))
print(game.make_move("G3","E2"))
print(game.make_move("G2","E2"))
game.display_game_board()
print(game.is_in_check("black"))
print(game.is_in_check("red"))
print(game._game_board.get_red_general_location())
print(game.get_game_state())
print(game._players_turn)