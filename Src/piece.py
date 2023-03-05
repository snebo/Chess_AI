import os


class Piece:
    def __init__(self, name, color, value, texture=None, texture_rect=None):
        self.name = name
        self.color = color
        value_sign = 1 if color == 'white' else -1
        self.value = value * value_sign
        self.moves = []
        self.moved = False
        self.texture = texture
        self.set_texture()
        self.texture_rect = texture_rect

    def set_texture(self, size=80):
        root = 'assets'
        # to find the image of the piece
        self.texture = os.path.join(
            f'Chess_AI\{root}\images\imgs-{size}px\{self.color}_{self.name}.png')

        # f.. meaninf folderssssss
        # assets/images/imgs-??px is the folder address
        # *color*_*imageName*.png is the image or file we're importing
        # {}in the string allows us to choose the exact file we want

    def add_move(self, move):
        self.moves.append(move)


class Pawn(Piece):
    def __init__(self, color):
        self.dir = -1 if color == 'white' else 1
        # super is our inheritor class 'pieces' and init is the init function in that class
        # the value is going to be useful for the ai in identifying and priotizing board pieces
        super().__init__('pawn', color, 1.0)


class Knight(Piece):
    def __init__(self, color):
        super().__init__('knight', color, 3.0, '')


class Bishop(Piece):
    def __init__(self, color):
        super().__init__('bishop', color, 3.001, '')


class Rook(Piece):
    def __init__(self, color):
        super().__init__('rook', color, 5.0, '')


class Queen(Piece):
    def __init__(self, color):
        super().__init__('queen', color, 9.0, '')


class King(Piece):
    def __init__(self, color):
        super().__init__('king', color, 10000.0, '')
