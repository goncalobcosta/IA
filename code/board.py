import pygame
from code.compound import *
from code.circle import *

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

class Board:
    def __init__(self, width, height, walls, blank, hero, compounds, red, green, blue, wallColor):
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

        path = "resources/images/circles/red_circle.png"
        self.redCircle = pygame.transform.smoothscale(pygame.image.load(path).convert_alpha(), (18, 18))

        path = "resources/images/circles/green_circle.png"
        self.greenCircle = pygame.transform.smoothscale(pygame.image.load(path).convert_alpha(), (18, 18))

        path = "resources/images/circles/green_circle.png"
        self.blueCircle = pygame.transform.smoothscale(pygame.image.load(path).convert_alpha(), (18, 18))
        
    def inBoard(self, pos):
        return (0 <= pos[0] < self.width and 0 <= pos[1] < self.height) and (pos not in self.blank) and (pos not in self.walls)
    
    
    def canMove(self, move, compound):
        for atom in compound.atoms:
            pos = atom.pos
            nextPos = (pos[0] + move[0], pos[1] + move[1])
            
            if not self.inBoard(nextPos): return False
            
            for other in self.compounds:
                if other != compound and other.isInPosition(nextPos) and ((len(compound.atoms) < len(other.atoms)) or not self.canMove(move, other)):
                    print("There is a compound that i cant push anymore")
                    return False
        return True
    
    def breakConnections(self, move):

        connections = []
        newCompounds = []

        for pos in self.red:
            atom1, atom2 = self.hero.getCandidates(move, pos)
            if (atom1 != [] and atom2 != []):
                connections.append((atom1[0], atom2[0]))
                self.hero.removeConnection(atom1[0], atom2[0])
                isolatedCompound = self.hero.checkIsolation()
                if isolatedCompound != []:
                    newCompound = Compound(isolatedCompound)
                    newCompounds.append(newCompound)
                    self.compounds.append(newCompound)
        return connections, newCompounds
    
    def reconnectCompounds(self, compounds):
        for compound in compounds:
            self.hero.atoms += compound.atoms
            self.compounds.remove(compound)

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
        
        self.connectIsolatedCompounds()

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
    
    def handlePushes(self, move, compound):
        compound.visited = True
        for atom in compound.atoms:
            pos = atom.pos
            nextPos = (pos[0] + move[0], pos[1] + move[1])
          
            for other in self.compounds:
                if not other.visited and other.isInPosition(nextPos) and (len(compound.atoms) >= len(other.atoms)) and self.canMove(move, compound):
                    self.handlePushes(move, other)
                    other.push(move)

    
    def connectIsolatedCompounds(self):
        allCompounds = self.compounds
        for i in range(len(allCompounds)-1):
            for j in range(i+1, len(allCompounds)):
                res = allCompounds[i].handleConnection(allCompounds[j])
                if res != []:
                    for tup in res:
                        tup[0].connect(tup[2], tup[3])
                    res[0][0].atoms += res[0][1].atoms
                    self.compounds.remove(res[0][1])       
        
    
    def connectCompounds(self):
        allCompounds = [self.hero] + self.compounds
        for i in range(len(allCompounds)-1):
            for j in range(i+1, len(allCompounds)):
                res = allCompounds[i].handleConnection(allCompounds[j])
                if res != []: 
                    for tup in res:
                        tup[0].connect(tup[2], tup[3])
                    res[0][0].atoms += res[0][1].atoms
                    self.compounds.remove(res[0][1])
        
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

        self.hero.draw(surface, self.width, self.height)

        for compound in self.compounds:
            compound.draw(surface, self.width, self.height)
        
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