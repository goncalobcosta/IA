import pygame
from Pieces.piece import Piece

class Wall(Piece):
    def __init__(self, x, y):
        super().__init__(connections=0, x=x, y=y)
    