import pygame
import sys

from const import *
from game import *

# means from the const file, import all (*=all)


class Main:
    # init is always called when we create an object
    def __init__(self) -> None:
        # initilize pygame.... always required
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        # pygame.display is to set the display/window and we use the values in const for that
        # caption is kinda like title
        pygame.display.set_caption('CHESS')
        self.game = Game()

    def mainLoop(self):
        # to stop us having to type self. ...
        game = self.game
        screen = self.screen
        dragger = self.game.dragger
        board = self.game.board

        # loops all through while application is running,
        while True:
            game.show_bg(screen)
            game.shop_moves(screen)
            game.show_pieces(screen)

            if dragger.dragging:
                dragger.update_blit(screen)

            # check if the user quits
            for event in pygame.event.get():

                # for click
                if event.type == pygame.MOUSEBUTTONDOWN:
                    dragger.update_mouse(event.pos)
                    # print(event.pos)

                    clicked_row = dragger.mouseY//SQSIZE
                    clicked_col = dragger.mouseX//SQSIZE
                    if board.squares[clicked_row][clicked_col].has_piece():
                        piece = board.squares[clicked_row][clicked_col].piece

                        board.cal_moves(piece, clicked_row, clicked_col)
                        dragger.save_initial(event.pos)
                        dragger.drag_piece(piece)

                        # show mwthods
                        game.show_bg(screen)
                        game.shop_moves(screen)
                        game.show_pieces(screen)
                # for drag
                elif event.type == pygame.MOUSEMOTION:
                    if dragger.dragging:
                        dragger.update_mouse(event.pos)

                        # show methods
                        game.show_bg(screen)
                        game.shop_moves(screen)
                        game.show_pieces(screen)
                        dragger.update_blit(screen)

                # for realeaase
                elif event.type == pygame.MOUSEBUTTONUP:
                    dragger.undrag_piece(piece)

                # quit
                elif event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            # this updates the screen
            # should be the last line of code in the main loop
            pygame.display.update()


main = Main()
# once we create this main instance, the init and then the
# main loop gets called
main.mainLoop()
