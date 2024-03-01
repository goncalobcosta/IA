from atom import *

class Compound:
    def __init__(self, atoms, isHeroCompound = False):
        self.atoms = atoms
        self.isHeroCompound = isHeroCompound
        
    def dfsDraw(self, surface, offX, offY, atom):
        atom.visited = True
        for neighbour in atom.connections:
            if not neighbour.visited:
                atom.drawConnection(surface, offX, offY, neighbour)
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