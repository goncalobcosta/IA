from atom import *

class Compound:
    def __init__(self, atoms, isHeroCompound = False):
        self.atoms = atoms
        self.isHeroCompound = isHeroCompound
        
    def dfsDraw(self, surface, offX, offY, atom):
        atom.visited = True
        for neighbour in atom.connections:
            if not neighbour.visited:
                isDoubleConnection = atom.connections.count(neighbour) == 2
                atom.drawConnection(surface, offX, offY, neighbour, isDoubleConnection)
                self.dfsDraw(surface, offX, offY, neighbour)
        
    def draw(self, surface, offX, offY):
        for atom in self.atoms:
            atom.visited = False
        self.dfsDraw(surface, offX, offY, self.atoms[0])
        for atom in self.atoms:
            atom.draw(surface, offX, offY)

           
    def addConnection(self, src, dest):
        src.addConnection(dest)
        dest.addConnection(src)
     
    def addAtom(self, atom):
        self.atoms.append(atom)
        
    def isInPosition(self, pos):
        return any(atom.isInPosition(pos) for atom in self.atoms)
        
    def move(self, move):
        for atom in self.atoms:
            atom.pos = (atom.pos[0] + move[0], atom.pos[1] + move[1])
            
    def connect(self, compound, src, dest):
        src.connect(dest)
        dest.connect(src) 
        self.atoms += compound.atoms       
        
    def handleConnection(self, compound):
        for atom in self.atoms:
            for atom2 in compound.atoms:
                if atom.canConnectTo(atom2): 
                   return (self, compound, atom, atom2) 
        
    def push(self, move):
        for atom in self.atoms:
            atom.move(move)
          
    def addConnection(self, atom1, atom2):
        if len(atom1.connections) < atom1.boundLimit and len(atom2.connections) < atom1.boundLimit:
            atom1.connect(atom2)
            atom2.connect(atom1)      
            
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