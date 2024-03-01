from atom import *

class Compound:
    def __init__(self, atoms, hero):
        self.atoms = atoms
        self.hero = hero
        
    def draw(self, surface, offX, offY):
        for atom in self.atoms:
            atom.draw(surface, offX, offY)
           
    def addConnection(self, src, dest):
        src.addConnection(dest)
        dest.addConnection(src)
     
    def addAtom(self, atom):
        self.atoms.append(atom)