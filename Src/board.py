from const import *
from square import Square
from piece import *
from move import Move


class Board:
    def __init__(self) -> None:
        # for every coloum, we add a list of 8 zeros
        self.squares = [[0, 0, 0, 0, 0, 0, 0, 0] for col in range(COLS)]
        self.lastMove = None
        self._create()
        self._add_pieces('white')
        self._add_pieces('black')

    # check 'move' or 'moves'
    def move(self, piece, move):
        initial = move.initial
        final = move.final

        # console board move update
        self.squares[initial.row][initial.col].piece = None
        self.squares[final.row][final.col].piece = piece

        piece.moved = True

        # clear valid moves
        piece.clear_move()
        # set last ove
        self.lastMove = move

    def validMove(self, piece, move):
        return move in piece.moves

    def cal_moves(self, piece, row, col):

        # This should calcaluate all possible or valid moves of a specific piece in
        # a specific position

        def king_moves():
            adjs = [
                (row-1, col),  # up
                (row-1, col+1),  # up-right
                (row-1, col-1),  # up-left
                (row, col-1),  # left
                (row, col+1),  # right
                (row+1, col),  # ...
                (row+1, col-1),
                (row+1, col+1)
            ]

            # normal moves
            for poss_move in adjs:
                poss_move_row, poss_move_col = poss_move

                if Square.in_range(poss_move_row, poss_move_col):
                    if self.squares[poss_move_row][poss_move_col].isempty_or_rival(piece.color):
                        # create squares opf new moves
                        initial = Square(row, col)
                        final = Square(poss_move_row, poss_move_col)

                        move = Move(initial, final)
                        piece.add_move(move)

            # casteling moves

        def pawn_moves():
            # step size for pawn
            steps = 1 if piece.moved else 2

            # vetical moves
            start = row + piece.dir
            end = (row + piece.dir * (1 + steps))
            for possible_move_row in range(start, end, piece.dir):
                if Square.in_range(possible_move_row):
                    if self.squares[possible_move_row][col].isempty():
                        # create initital and final move squares
                        initial = Square(row, col)
                        final = Square(possible_move_row, col)

                        # create a move
                        move = Move(initial, final)
                        # append new move
                        piece.add_move(move)
                    # if blocked
                    else:
                        break
                # not in range
                else:
                    break

            # diagonal moves
            possible_move_row = row + piece.dir
            possible_move_cols = [col-1, col+1]
            for possible_move_col in possible_move_cols:
                if Square.in_range(possible_move_row, possible_move_col):
                    if self.squares[possible_move_row][possible_move_col].has_rival_piece(piece.color):
                        initial = Square(row, col)
                        final = Square(possible_move_row, possible_move_col)

                        move = Move(initial, final)
                        # append new move
                        piece.add_move(move)

        def knight_moves():
            # at center has 8 possible moves
            possible_moves = [
                (row-2, col+1), (row-2, col-1),
                (row+2, col-1), (row+2, col+1),
                (row-1, col+2), (row-1, col-2),
                (row+1, col+2), (row+1, col-2)
            ]

            for possible_move in possible_moves:
                possible_moves_row, possible_moves_col = possible_move

                if Square.in_range(possible_moves_row, possible_moves_col):
                    if self.squares[possible_moves_row][possible_moves_col].isempty_or_rival(piece.color):
                        # creating new squares for moves
                        initial = Square(row, col)
                        final = Square(possible_moves_row, possible_moves_col)

                        # create moves
                        move = Move(initial, final)
                        # append move
                        piece.add_move(move)

        def straight_line_moves(incrs):
            for inc in incrs:
                row_inc, col_inc = (inc)
                poss_move_row = row + row_inc
                poss_move_col = col + col_inc

                while True:
                    if Square.in_range(poss_move_row, poss_move_col):
                        # checks if there are avaliavble boards
                        # create squares of new moves
                        initial = Square(row, col)
                        final = Square(poss_move_row, poss_move_col)

                        move = Move(initial, final)

                        # check if the next square is empty
                        if self.squares[poss_move_row][poss_move_col].isempty():
                            # append new move
                            piece.add_move(move)

                        elif self.squares[poss_move_row][poss_move_col].has_rival_piece(piece.color):
                            # create a new move
                            piece.add_move(move)
                            break

                        elif self.squares[poss_move_row][poss_move_col].has_team_piece(piece.color):
                            break

                    else:
                        break

                    # incrementing the increments
                    poss_move_row = poss_move_row + row_inc
                    poss_move_col = poss_move_col + col_inc

        if isinstance(piece, Pawn):
            pawn_moves()

        elif isinstance(piece, Knight):
            knight_moves()

        elif isinstance(piece, Bishop):
            straight_line_moves([
                (-1, 1),  # up-right diagonal
                (-1, -1),  # up left diognal
                (1, 1),  # down right coner
                (1, -1)  # down left corner
            ])

        elif isinstance(piece, Rook):
            straight_line_moves([
                (-1, 0),  # up
                (0, 1),  # left
                (1, 0),  # down
                (0, -1)  # right
            ])

        elif isinstance(piece, Queen):
            straight_line_moves([
                (-1, 1),  # up-right diagonal
                (-1, -1),  # up left diognal
                (1, 1),  # down right coner
                (1, -1),  # down left corner

                (-1, 0),  # up
                (0, 1),  # left
                (1, 0),  # down
                (0, -1)  # right
            ])

        elif isinstance(piece, King):
            king_moves()

    def _create(self):
        # look at it like table row and table data
        for row in range(ROWS):
            for col in range(COLS):
                # says what is in each table
                self.squares[row][col] = Square(row, col)

    def _add_pieces(self, color):
        row_pawn, row_other = (6, 7) if color == 'white' else (1, 0)
        # setting the position of blacks and white piecies

        # the first row of pawns
        for col in range(COLS):
            self.squares[row_pawn][col] = Square(row_pawn, col, Pawn(color))

        # knights
        # using from 0 counting to arrange the pi3eces
        self.squares[row_other][1] = Square(row_other, 1, Knight(color))
        self.squares[row_other][6] = Square(row_other, 6, Knight(color))

        # Biahops
        self.squares[row_other][2] = Square(row_other, 2, Bishop(color))
        self.squares[row_other][5] = Square(row_other, 5, Bishop(color))

        # for testing self.squares[5][7] = Square(7, 5, Bishop(color))

        # rook
        self.squares[row_other][0] = Square(row_other, 0, Rook(color))
        self.squares[row_other][7] = Square(row_other, 7, Rook(color))

        # queen
        self.squares[row_other][3] = Square(row_other, 3, Queen(color))

        # King
        self.squares[row_other][4] = Square(row_other, 4, King(color))
