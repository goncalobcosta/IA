from itertools import combinations
from code.atom import *

class Compound:
    def __init__(self, atoms, isHeroCompound = False):
        self.atoms = atoms
        self.isHeroCompound = isHeroCompound
        self.pushed = False
        self.visited = False
        
    def dfsDraw(self, surface, offX, offY, atom):
        atom.visited = True
        for neighbour in atom.connections:
            atom.drawConnection(surface, offX, offY, neighbour, atom.connections.count(neighbour))
            if not neighbour.visited:
                self.dfsDraw(surface, offX, offY, neighbour)
        
    def draw(self, surface, offX, offY):
        for atom in self.atoms:
            atom.visited = False
        self.dfsDraw(surface, offX, offY, self.atoms[0])
        for atom in self.atoms:
            atom.draw(surface, offX, offY)
    
     
    def addAtom(self, atom):
        self.atoms.append(atom)
        
    def isInPosition(self, pos):
        return any(atom.isInPosition(pos) for atom in self.atoms)
        
    def move(self, move):
        for atom in self.atoms:
            atom.pos = (atom.pos[0] + move[0], atom.pos[1] + move[1])
        self.checkConnections()
            
    def connect(self, src, dest):
        src.connect(dest)
        dest.connect(src) 
        
    def handleConnection(self, compound):
        res = []
        for atom in self.atoms:
            for atom2 in compound.atoms:
                if atom.canConnectTo(atom2): 
                   res.append((atom, atom2))
        return res
        
    def push(self, move):
        for atom in self.atoms:
            atom.move(move)
          
    def addConnection(self, atom1, atom2):
        if len(atom1.connections) < atom1.boundLimit and len(atom2.connections) < atom2.boundLimit:
            atom1.connect(atom2)
            atom2.connect(atom1)  
    
    def removeConnection(self, atom1, atom2):
        if atom1 in atom2.connections:
            atom1.disconnect(atom2)
            atom2.disconnect(atom1)   
            
    def getCandidates(self, move, pos):
        x, y = pos 
        upLeft = [atom for atom in self.atoms if atom.pos == (x, y)]
        upRight = [atom for atom in self.atoms if atom.pos == (x+1, y)]
        downLeft = [atom for atom in self.atoms if atom.pos == (x, y+1)]
        downRight = [atom for atom in self.atoms if atom.pos == (x+1, y+1)]
       
        if move == UP:
            return downLeft, downRight
        elif move == DOWN:
            return upLeft, upRight
        elif move == LEFT:
            return upRight, downRight
        return upLeft, downLeft
    
    def dfs(self, atom):
        atom.visited = True
        for neighbour in atom.connections:
            if not neighbour.visited:
                self.dfs(neighbour)
    
    def checkIsolation(self):
        for atom in self.atoms:
            atom.visited = False
                    
        self.dfs(self.atoms[0])
        
        isolated = [atom for atom in self.atoms if not atom.visited]
        self.atoms = [atom for atom in self.atoms if atom.visited]
        
        return isolated
    
    def reconnect(self, connections):
        for connection in connections:
            atom1, atom2 = connection
            self.connect(atom1, atom2)
            
    def rotate(self, move):
        dx, dy = move
        for i in range(len(self.atoms) - 1, 0, -1):
            atom = self.atoms[i]
            if atom.isHero: continue
            else:
                x, y = self.atoms[i-1].pos
                atom.pos = (x-dx, y-dy)
    
    def dfsSnake(self, atom, current_path):
        atom.visited = True
        current_path.append(atom)

        for a in atom.connections:
            if not a.visited:
                self.dfsSnake(a, current_path)
                break

        return current_path

    def isSnake(self):
        for atom in self.atoms:
            atom.visited = False

        hero = self.atoms[0]
        path = self.dfsSnake(hero, [])
        last = path[-1]

        no = [atom for atom in self.atoms if not atom.visited]
        if no != []:
            return False
        
        return last not in hero.connections if len(path) > 2 else True


    def checkConnections(self):
        for atom1, atom2 in combinations(self.atoms, 2):
            if(atom1.canConnectTo(atom2) and (atom2 not in atom1.connections)):
                atom1.connect(atom2)
                atom2.connect(atom1)

    def fullyConnected(self):
        for atom in self.atoms:
            if len(atom.connections) < atom.boundLimit:
                return False
        return True