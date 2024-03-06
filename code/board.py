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
        
    def inBoard(self, pos):
        return (0 <= pos[0] < self.width and 0 <= pos[1] < self.height) and (pos not in self.blank) and (pos not in self.walls)
   
    def canMove(self, move, compound):
        for atom in compound.atoms:
            pos = atom.pos
            nextPos = (pos[0] + move[0], pos[1] + move[1])
            
            if not self.inBoard(nextPos): 
                return False
            
            for other in self.compounds:
                if other != compound and other.isInPosition(nextPos) and (not self.canMove(move, other)):
                    return False
        return True
    
    def breakConnections(self, move):
        
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
    
    def reconnectCompounds(self, compounds):
        for (oldCompound, newCompound) in compounds:
            oldCompound.atoms += newCompound.atoms
            self.compounds.remove(newCompound)

    def handleMove(self, move):
        
        heroAtom = self.hero.atoms[0]
        nextPos = (heroAtom.pos[0] + move[0], heroAtom.pos[1] + move[1])
        if not self.inBoard(nextPos) : return

        brokenConnections, newCompounds = self.breakConnections(move)

        if not self.canMove(move, self.hero): 
            self.hero.reconnect(brokenConnections)
            self.reconnectCompounds(newCompounds)
            return 
        
        self.handleGreenCircles(move)
        self.handleBlueCircles(move)

        for compound in self.compounds: 
           compound.visited = False 

        self.handlePushes(move, self.hero)
        
        self.hero.move(move)
        self.connectCompounds()
         
    def handleGreenCircles(self, move):
        allCompounds = [self.hero] + self.compounds
        for pos in self.green:
            for compound in allCompounds:
                atom1, atom2 = compound.getCandidates(move, pos)
                if (atom1 != [] and atom2 != []):
                    compound.addConnection(atom1[0], atom2[0])

    def handleBlueCircles(self, move):
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

    def handlePushes(self, move, compound):
        compound.visited = True
        for atom in compound.atoms:
            pos = atom.pos
            nextPos = (pos[0] + move[0], pos[1] + move[1])
          
            for other in self.compounds:
                if not other.visited and other.isInPosition(nextPos) and self.canMove(move, compound):
                    self.handlePushes(move, other)
                    other.push(move)
  
    def connectCompounds(self):
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
        
    def drawBoard(self, surface):
        for y in range(self.height):
            for x in range(self.width):
                if (x, y) in self.walls:
                    pygame.draw.rect(surface, self.wallColor, ((WIDTH - self.width * SQUARE) // 2 + x*SQUARE, (HEIGHT - self.height * SQUARE) // 2 + y*SQUARE, 46, 46))
                elif (x, y) not in self.blank:
                    pygame.draw.rect(surface, BACKGROUND, ((WIDTH - self.width * SQUARE) // 2 + x*SQUARE, (HEIGHT - self.height * SQUARE) // 2 + y*SQUARE, 46, 46))
      
    def draw(self, surface):
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

    def win(self):
        allCompounds = [self.hero] + self.compounds
        for compound in allCompounds:
            if not compound.fullyConnected():
                return False
        return True

    def printStat(self):
        print("My hero is")
        for atom in self.hero.atoms:
            x = []
            for con in atom.connections:
                x.append(con.pos)
            print(atom.pos, x)
        print("=========")
        for i in self.compounds:
            l = []
            for a in i.atoms:
                l += [a.pos]
            print(l)
        print("=========")

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return (self.name == other.name and
                    self.hero == other.hero and
                    self.compounds == other.compounds)
        else:
            return False
        
    def copy(self):
        hero = self.hero.copy()
        compounds = []
        for compound in self.compounds:
            compounds.append(compound.copy())
        
        board = self.__class__(self.width, self.height, self.walls, self.blank, hero, compounds, self.red, self.green, self.blue, self.wallColor, self.name)
        return board
        
    def lose(self):
        return self.hero.fullyConnected()
