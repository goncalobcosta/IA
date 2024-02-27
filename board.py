import pygame

COR_BRANCA = (255, 255, 255)
COR_CINZENTA = (180, 180, 180)

class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid = [[None] * width for _ in range(height)]

    def is_valid_position(self, x, y):
        return 0 <= x < self.width and 0 <= y < self.height

    def add_piece(self, piece, x, y):
        if self.is_valid_position(x, y):
            self.grid[y][x] = piece
            piece.set_position(x, y)

    def move_piece(self, piece, new_x, new_y):
        if self.is_valid_position(new_x, new_y):
            old_x, old_y = piece.position
            self.grid[old_y][old_x] = None
            self.grid[new_y][new_x] = piece
            piece.set_position(new_x, new_y)

    def get_piece_at(self, x, y):
        if self.is_valid_position(x, y):
            return self.grid[y][x]
        return None

    def draw(self, surface):
        # Draw the grid
        for y in range(self.height):
            for x in range(self.width):
                pygame.draw.rect(surface, COR_BRANCA , (x*50, y*50, 50, 50), 2)
                pygame.draw.rect(surface, COR_CINZENTA, (x*50.5, y*50.5, 46, 46))
