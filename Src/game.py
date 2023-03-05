import pygame
from const import *
from board import Board
from piece import *
from dragger import *


## ____RENDERS BOARD AND PIECES____##


class Game:
    def __init__(self) -> None:
        self.board = Board()
        self.dragger = Dragger()

        # show methods

    def show_bg(self, surface):
        for row in range(ROWS):
            for col in range(COLS):
                if (row + col) % 2 == 0:
                    color = (234, 235, 200)  # light green
                else:
                    color = (119, 154, 88)  # dark green

                rect = (col*SQSIZE, row*SQSIZE, SQSIZE, SQSIZE)

                pygame.draw.rect(surface, color, rect)

    def show_pieces(self, surface):
        for row in range(ROWS):
            for col in range(COLS):
                # check if there is a piece
                # by default there should be

                if self.board.squares[row][col].has_piece():
                    # if a piece is there, do this
                    piece = self.board.squares[row][col].piece
                    # save the piece info
                    # get and paste the image of that piece centered

                    # bliting all pieces
                    if piece is not self.dragger.piece:

                        piece.set_texture(size=80)
                        img = pygame.image.load(piece.texture)
                        image_center = col*SQSIZE + SQSIZE//2, row*SQSIZE + SQSIZE//2
                        Piece.texture_rect = img.get_rect(center=image_center)
                        surface.blit(img, Piece.texture_rect)
                        # crying smile face.. after hours, finally did it
                        # issues were here and in the texture load fileswssss

    def shop_moves(self, surface):
        if self.dragger.dragging:
            piece = self.dragger.piece
            # loop all valid movs
            for moves in piece.moves:
                # color
                color = '#c86464' if (
                    moves.final.row + moves.final.col) % 2 == 0 else '#c84646'
                # rect
                rect = (moves.final.col * SQSIZE,
                        moves.final.row * SQSIZE, SQSIZE, SQSIZE)
                # blit
                pygame.draw.rect(surface, color, rect)
