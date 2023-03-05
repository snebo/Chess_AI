import pygame
from const import *


class Dragger:
    def __init__(self) -> None:
        self.mouseX = 0
        self.mouseY = 0
        self.initialRow = 0
        self.initialCol = 0
        self.piece = None
        self.dragging = False

    # blitz method
    def update_blit(self, surface):
        # replace the texture
        self.piece.set_texture(size=128)
        texture = self.piece.texture
        # image
        img = pygame.image.load(texture)

        # rext
        img_center = (self.mouseX, self.mouseY)
        self.piece.texture_rect = img.get_rect(center=img_center)

        # blit
        surface.blit(img, self.piece.texture_rect)

    # others

    def update_mouse(self, pos):
        self.mouseX, self.mouseY = pos  # (X,Y)

    def save_initial(self, pos):
        self.initialRow = pos[1]//SQSIZE
        self.initialCol = pos[0] // SQSIZE

    def drag_piece(self, piece):
        self.piece = piece
        self.dragging = True

    def undrag_piece(self, piece):
        self.piece = None
        self.dragging = False
