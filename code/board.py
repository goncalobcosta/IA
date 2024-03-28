import pygame
from code.compound import *

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARK_GRAY = (150, 150, 150)
GRAY = (192, 192, 192)
RED = (255, 138, 128)
YELLOW = (254, 216, 119)
BLUE = (166, 197, 254)
GREEN = (175, 219, 140)
BACKGROUND = (243, 243, 243)
GOLD = (218, 165, 32)

class Board:
    def __init__(self, width, height, walls, blank, hero, compounds, red, green, blue, wallColor, name):
        self.width = width
        self.height = height
        self.walls = walls
        self.blank = blank
        self.hero = hero
        self.compounds = compounds
        self.red = red
        self.green = green
        self.blue = blue
        self.wallColor = wallColor
        self.name = name

        path = "resources/images/circles/red_circle.png"
        self.redCircle = pygame.transform.smoothscale(pygame.image.load(path).convert_alpha(), (18, 18))

        path = "resources/images/circles/green_circle.png"
        self.greenCircle = pygame.transform.smoothscale(pygame.image.load(path).convert_alpha(), (18, 18))

        path = "resources/images/circles/blue_circle.png"
        self.blueCircle = pygame.transform.smoothscale(pygame.image.load(path).convert_alpha(), (18, 18))
        
    def inBoard(self, pos : tuple[int, int]) -> bool:
        """
        Check if a position is inside the board.

        Args:
            pos (tuple): The position to check.

        Returns:
            bool: True if the position is inside the board and not a wall or blank space, False otherwise.
        """
        return (0 <= pos[0] < self.width and 0 <= pos[1] < self.height) and (pos not in self.blank) and (pos not in self.walls)
   
    def canMove(self, move : tuple[int, int], compound : Compound) -> bool:
        """
        Check if a compound can make a move.

        Args:
            move (tuple): The move to make.
            compound (Compound): The compound to move.

        Returns:
            bool: True if the compound can make the move, False otherwise.
        """
        for atom in compound.atoms:
            pos = atom.pos
            nextPos = (pos[0] + move[0], pos[1] + move[1])
            
            if not self.inBoard(nextPos): 
                return False
            
            for other in self.compounds:
                if other != compound and other.isInPosition(nextPos) and (not self.canMove(move, other)):
                    return False
        return True
    
    def breakConnections(self, move : tuple[int, int]) -> tuple[list[Atom], list[Atom]]:
        """
        Break the connections between atoms after a move.

        Args:
            move (tuple): The move made by the player.

        Returns:
            tuple: A tuple containing two lists - the first list contains the connections broken,
                   and the second list contains tuples of old and new compounds formed after the connections are broken.
        """
        allCompounds = [self.hero] + self.compounds

        connections = []
        newCompounds = []

        for compound in allCompounds:
            for pos in self.red:
                atom1, atom2 = compound.getCandidates(move, pos)
                if (atom1 != [] and atom2 != []):
                    connections.append((atom1[0], atom2[0]))
                    compound.removeConnection(atom1[0], atom2[0])
                    isolatedCompound = compound.checkIsolation()
                    if isolatedCompound != []:
                        newCompound = Compound(isolatedCompound)
                        newCompounds.append((compound, newCompound))
                        self.compounds.append(newCompound)
        return connections, newCompounds
    
    def reconnectCompounds(self, compounds : list[Compound]):
        """
        Reconnect the compounds broken during the game.

        Args:
            compounds (list): A list of tuples containing old and new compounds formed after breaking connections.
        """
        for (oldCompound, newCompound) in compounds:
            oldCompound.atoms += newCompound.atoms
            self.compounds.remove(newCompound)

    def handleMove(self, move : tuple[int, int]) -> bool:
        """
        Handle the movement of the hero atom.

        Args:
            move (tuple): The move to be made by the hero.

        Returns:
            bool: True if the move is valid and successfully executed, False otherwise.
        """
        heroAtom = self.hero.atoms[0]
        nextPos = (heroAtom.pos[0] + move[0], heroAtom.pos[1] + move[1])
        if not self.inBoard(nextPos) : return

        brokenConnections, newCompounds = self.breakConnections(move)

        if not self.canMove(move, self.hero): 
            self.hero.reconnect(brokenConnections)
            self.reconnectCompounds(newCompounds)
            return False
        
        self.handleGreenCircles(move)
        self.handleBlueCircles(move)

        for compound in self.compounds: 
           compound.visited = False 

        self.handlePushes(move, self.hero)
        
        self.hero.move(move)
        self.connectCompounds()
        
        return True
         
    def handleGreenCircles(self, move : tuple[int, int]):
        """
        Handle the effects of green circles after a move.

        Args:
            move (tuple): The move made by the hero.
        """
        allCompounds = [self.hero] + self.compounds
        for pos in self.green:
            for compound in allCompounds:
                atom1, atom2 = compound.getCandidates(move, pos)
                if (atom1 != [] and atom2 != []):
                    compound.addConnection(atom1[0], atom2[0])

    def handleBlueCircles(self, move : tuple[int, int]):
        """
        Handle the effects of blue circles after a move.

        Args:
            move (tuple): The move made by the hero.
        """
        if not self.hero.isSnake(): return
        nextPos = (self.hero.atoms[0].pos[0] + move[0], self.hero.atoms[0].pos[1] + move[1])
        for atom in self.hero.atoms:
            if atom.isInPosition(nextPos):
                return False
            
        for pos in self.blue:
            atom1, atom2 = self.hero.getCandidates(move, pos)
            if (atom1 != [] and atom2 != []):
                self.hero.rotate(move)
                return

    def handlePushes(self, move : tuple[int, int], compound : Compound):
        """
        Recursively handle the pushing of atoms in the specified direction.

        Args:
            move (tuple): The direction of the push.
            compound (Compound): The compound of atoms to be pushed.
        """
        compound.visited = True
        for atom in compound.atoms:
            pos = atom.pos
            nextPos = (pos[0] + move[0], pos[1] + move[1])
          
            for other in self.compounds:
                if not other.visited and other.isInPosition(nextPos) and self.canMove(move, compound):
                    self.handlePushes(move, other)
                    other.push(move)
  
    def connectCompounds(self):
        """
        Connect compounds together based on their positions after pushing.
        """
        allCompounds = [self.hero] + self.compounds
        removed = []
        for compound1 in allCompounds:
            for compound2 in allCompounds:
                if ((compound1 == compound2) or (compound2 in removed) or (compound1 in removed)): continue

                res = compound1.handleConnection(compound2)
                if res != []: 
                    for atom1,atom2 in res:
                        compound1.connect(atom1, atom2)
                    compound1.atoms += compound2.atoms
                    removed.append(compound2)
                    self.compounds.remove(compound2)
        
    def win(self) -> bool:
        """
        Check if all compounds are fully connected, indicating a win condition.

        Returns:
            bool: True if all compounds are fully connected, False otherwise.
        """
        allCompounds = [self.hero] + self.compounds
        for compound in allCompounds:
            if not compound.fullyConnected():
                return False
        return True

    def greedyMove(self, move : tuple[int, int]) -> int:
        """
        Calculate the greedy move based on the distance between the hero compound and other compounds.

        Args:
            move (tuple): The direction of movement.

        Returns:
            float: The distance between the hero compound and the nearest other compound.
        """
        distance = float('inf')
        if self.compounds == []: return 0

        for atom in self.hero.atoms:
            atom.pos = atom.pos[0] + move[0], atom.pos[1] + move[1]

        for compound in self.compounds:
            d = self.hero.distance(compound)
            if (d < distance):
                distance = d

        for atom in self.hero.atoms:
            atom.pos = atom.pos[0] - move[0], atom.pos[1] - move[1]

        return distance

    def closestCircle(self, move : tuple[int, int]) -> int:
        """
        Calculate the distance from the hero compound to the closest circle.

        Args:
            move (tuple): The direction of movement.

        Returns:
            float: The Manhattan distance from the hero compound to the closest circle.
        """
        distance = float('inf')
        circles = self.red.union(self.blue, self.green)
        if (len(circles) == 0): return 0
        
        for atom in self.hero.atoms:
            atom.pos = atom.pos[0] + move[0], atom.pos[1] + move[1]
            for circle in circles:
                d = abs(atom.pos[0] - circle[0]) + abs(atom.pos[1] - circle[1])
                if (d < distance):
                    distance = d
            atom.pos = atom.pos[0] - move[0], atom.pos[1] - move[1]

        return distance

    def drawBoard(self, surface):
        """
        Draw the board.
        """
        for y in range(self.height):
            for x in range(self.width):
                if (x, y) in self.walls:
                    pygame.draw.rect(surface, self.wallColor, ((WIDTH - self.width * SQUARE) // 2 + x*SQUARE, (HEIGHT - self.height * SQUARE) // 2 + y*SQUARE, 46, 46))
                elif (x, y) not in self.blank:
                    pygame.draw.rect(surface, BACKGROUND, ((WIDTH - self.width * SQUARE) // 2 + x*SQUARE, (HEIGHT - self.height * SQUARE) // 2 + y*SQUARE, 46, 46))
      
    def draw(self, surface):
        """
        Draw the board and the pieces.
        """
        self.drawBoard(surface)

        for (x, y) in self.red:
            surface.blit(self.redCircle, ((WIDTH - self.width * 50) // 2 + x*50 + 39, (HEIGHT - self.height * 50) // 2 + y*50 + 39))

        for (x, y) in self.green:
            surface.blit(self.greenCircle, ((WIDTH - self.width * 50) // 2 + x*50 + 41, (HEIGHT - self.height * 50) // 2 + y*50 + 41))

        for (x, y) in self.blue:
            surface.blit(self.blueCircle, ((WIDTH - self.width * 50) // 2 + x*50 + 41.5, (HEIGHT - self.height * 50) // 2 + y*50 + 41.5))

        self.hero.draw(surface, self.width, self.height)

        for compound in self.compounds:
            compound.draw(surface, self.width, self.height)


    def __eq__(self, other):
        """
        Check if two boards are equal.

        Args:
            other (Board): The other board to compare with.

        Returns:
            bool: True if the boards are equal, False otherwise.
        """
        if isinstance(other, self.__class__):
            return (self.name == other.name and
                    self.hero == other.hero and
                    self.compounds == other.compounds)
        else:
            return False
        
    def copy(self):
        """
        Create a deep copy of the board.

        Returns:
            Board: A deep copy of the board.
        """
        hero = self.hero.copy()
        compounds = []
        for compound in self.compounds:
            compounds.append(compound.copy())
        
        board = self.__class__(self.width, self.height, self.walls, self.blank, hero, compounds, self.red, self.green, self.blue, self.wallColor, self.name)
        return board
        
    def __lt__(self, other):
        """
        Compare two boards based on their cost and heuristic estimate.

        Args:
            other (Board): The other board to compare with.

        Returns:
            bool: True if self is less than other, False otherwise.
        """
        if (self.cost + self.heuristic_estimate == other.cost + other.heuristic_estimate):
            return self.heuristic_estimate < other.heuristic_estimate
        return self.cost + self.heuristic_estimate < other.cost + other.heuristic_estimate
    
    def __hash__(self):
        return hash((self.hero, tuple(self.compounds)))
