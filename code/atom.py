import pygame

He = ("helium", 0)
H = ("hydrogen", 1)
O = ("oxygen", 2)
N = ("nitrogen", 3)
C = ("carbon", 4)

WIDTH = 800
HEIGHT = 600
SQUARE = 50

# DIRECTIONS
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

DIRECTIONS = [UP, DOWN, LEFT, RIGHT]


class Atom:
    def __init__(self, atom : tuple[str, int], pos : tuple[int, int], isHero: bool = False):
        self.name, self.boundLimit, = atom
        self.pos = pos
        self.connections = []
        self.isHero = isHero  
        self.visited = False
        path = "resources/images/atoms/" + self.name + "/" + ("hero" if self.isHero else self.name) + str(self.boundLimit - len(self.connections)) + ".png"
        self.image = pygame.transform.smoothscale(pygame.image.load(path).convert_alpha(), (50, 50))

    def draw(self, surface, offX : int, offY : int):
        """
        Draw the atom on a given surface.

        Parameters:
        - surface: The surface on which to draw the atom.
        - offX (int): Offset in the x-direction.
        - offY (int): Offset in the y-direction.
        """
        x, y = self.pos
        surface.blit(self.image, ((WIDTH - offX * SQUARE) // 2 + x*SQUARE, ((HEIGHT - offY * SQUARE) // 2 + y*SQUARE)))
    
    def updateImage(self):
        """
        Update the atom image based on its connections.
        """
        path = "resources/images/atoms/" + self.name + "/" + ("hero" if self.isHero else self.name) + str(self.boundLimit - len(self.connections)) + ".png"
        self.image = pygame.transform.smoothscale(pygame.image.load(path).convert_alpha(), (50, 50))
        
    def connect(self, atom):
        """
        Connect the atom to another atom.

        Parameters:
        - atom (Atom): The atom to connect to.
        """
        self.connections.append(atom)
        self.updateImage()
    
    def disconnect(self, atom):
        """
        Disconnect the atom from another atom.

        Parameters:
        - atom (Atom): The atom to disconnect from.
        """
        self.connections.remove(atom)
        self.updateImage()
    
    def move(self, move : tuple[int, int]):
        """
        Move the atom by a given displacement.

        Parameters:
        - move (tuple): A tuple containing the displacement in the x and y directions.
        """
        self.pos = (self.pos[0] + move[0], self.pos[1] + move[1])
    
    def isInPosition(self, pos : tuple[int, int]) -> bool:
        """
        Check if the atom is in a given position.

        Parameters:
        - pos (tuple): A tuple containing the position coordinates to check.

        Returns:
        - bool: True if the atom is in the given position, False otherwise.
        """
        return self.pos == pos
    
    def isNextTo(self, atom) -> bool:
        """
        Check if the atom is next to another atom.

        Parameters:
        - atom (Atom): The atom to check adjacency with.

        Returns:
        - bool: True if the atom is adjacent to the other atom, False otherwise.
        """
        x1, y1 = self.pos
        x2, y2 = atom.pos
        if (x1 == x2 and abs(y1 - y2) == 1): return True
        if (y1 == y2 and abs(x1 - x2) == 1): return True
        return False
    
    def canConnectTo(self, atom) -> bool:
        """
        Check if the atom can connect to another atom.

        Parameters:
        - atom (Atom): The atom to check connectivity with.

        Returns:
        - bool: True if the atom can connect to the other atom, False otherwise.
        """
        return self.isNextTo(atom) and len(self.connections) < self.boundLimit and len(atom.connections) < atom.boundLimit
        
    def manhattanDistance(self, atom) -> int:
        """
        Calculate the Manhattan distance between the atom and another atom.

        Parameters:
        - atom (Atom): The other atom.

        Returns:
        - int: The Manhattan distance between the two atoms.
        """
        return abs(self.pos[0] - atom.pos[0]) + abs(self.pos[1] - atom.pos[1])
        
    def drawConnection(self, surface, offX : int, offY : int, atom, connections : int):
        """
        Draw a connection line between the atom and another atom on a surface.

        Parameters:
        - surface: The surface on which to draw the connection line.
        - offX (int): Offset in the x-direction.
        - offY (int): Offset in the y-direction.
        - atom (Atom): The other atom to connect to.
        - connections (int): Number of connections between the atoms.
        """
        direction = (atom.pos[0] - self.pos[0], atom.pos[1] - self.pos[1])
        if (connections == 2):
            if direction == UP:
                pygame.draw.rect(surface, (0,0,0), ((WIDTH - offX * SQUARE) // 2 + atom.pos[0]*SQUARE + 17, ((HEIGHT - offY * SQUARE) // 2 + atom.pos[1]*SQUARE + 22), 5, 50))
                pygame.draw.rect(surface, (0,0,0), ((WIDTH - offX * SQUARE) // 2 + atom.pos[0]*SQUARE + 27, ((HEIGHT - offY * SQUARE) // 2 + atom.pos[1]*SQUARE + 22), 5, 50))
            elif direction == DOWN:
                pygame.draw.rect(surface, (0,0,0), ((WIDTH - offX * SQUARE) // 2 + self.pos[0]*SQUARE + 17, ((HEIGHT - offY * SQUARE) // 2 + self.pos[1]*SQUARE + 22), 5, 50))
                pygame.draw.rect(surface, (0,0,0), ((WIDTH - offX * SQUARE) // 2 + self.pos[0]*SQUARE + 27, ((HEIGHT - offY * SQUARE) // 2 + self.pos[1]*SQUARE + 22), 5, 50))
            elif direction == LEFT:
                pygame.draw.rect(surface, (0,0,0), ((WIDTH - offX * SQUARE) // 2 + atom.pos[0]*SQUARE + 22, ((HEIGHT - offY * SQUARE) // 2 + atom.pos[1]*SQUARE + 17), 50, 5))
                pygame.draw.rect(surface, (0,0,0), ((WIDTH - offX * SQUARE) // 2 + atom.pos[0]*SQUARE + 22, ((HEIGHT - offY * SQUARE) // 2 + atom.pos[1]*SQUARE + 27), 50, 5))
            elif direction == RIGHT:
                pygame.draw.rect(surface, (0,0,0), ((WIDTH - offX * SQUARE) // 2 + self.pos[0]*SQUARE + 22, ((HEIGHT - offY * SQUARE) // 2 + self.pos[1]*SQUARE + 17), 50, 5))
                pygame.draw.rect(surface, (0,0,0), ((WIDTH - offX * SQUARE) // 2 + self.pos[0]*SQUARE + 22, ((HEIGHT - offY * SQUARE) // 2 + self.pos[1]*SQUARE + 27), 50, 5))
        else:
            if direction == UP:
                pygame.draw.rect(surface, (0,0,0), ((WIDTH - offX * SQUARE) // 2 + atom.pos[0]*SQUARE + 22, ((HEIGHT - offY * SQUARE) // 2 + atom.pos[1]*SQUARE + 22), 5, 50))
            elif direction == DOWN:
                pygame.draw.rect(surface, (0,0,0), ((WIDTH - offX * SQUARE) // 2 + self.pos[0]*SQUARE + 22, ((HEIGHT - offY * SQUARE) // 2 + self.pos[1]*SQUARE + 22), 5, 50))
            elif direction == LEFT:
                pygame.draw.rect(surface, (0,0,0), ((WIDTH - offX * SQUARE) // 2 + atom.pos[0]*SQUARE + 22, ((HEIGHT - offY * SQUARE) // 2 + atom.pos[1]*SQUARE + 22), 50, 5))
            elif direction == RIGHT:
                pygame.draw.rect(surface, (0,0,0), ((WIDTH - offX * SQUARE) // 2 + self.pos[0]*SQUARE + 22, ((HEIGHT - offY * SQUARE) // 2 + self.pos[1]*SQUARE + 22), 50, 5))
    
    def __eq__(self, other):
        """
        Check if the atom is equal to another atom.

        Parameters:
        - other (Atom): The other atom.

        Returns:
        - bool: True if the two atoms are equal, False otherwise.
        """
        if isinstance(other, self.__class__):
            if (len(self.connections) != len(other.connections)):
                return False
            for atom in self.connections:
                name, pos = atom.name, atom.pos
                has = False
                for atom2 in other.connections:
                    if atom2.name == name and atom2.pos == pos:
                        has = True
                        break
                if not has:
                    return False
            return self.name == other.name and self.pos == other.pos
        else:
            return False
    