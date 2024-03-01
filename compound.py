from atom import *

class Compound:
    def __init__(self, atoms, isHeroCompound = False):
        self.atoms = atoms
        self.isHeroCompound = isHeroCompound
        
    def draw(self, surface, offX, offY):
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