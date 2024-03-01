def handlePushes(self, move):
        atomsToPush = {}
        for pos in self.compound.keys():
            nextPos = (pos[0] + move[0], pos[1] + move[1])
            while self.atoms.get(nextPos) is not None:
                atom = self.atoms.get(nextPos)
                nextPos = (nextPos[0] + move[0], nextPos[1] + move[1])
                atomsToPush[nextPos] = atom
        self.pushAtoms(atomsToPush)
    
    def pushAtoms(self, updated):
        
        for (pos, atom) in self.atoms.items():
            if atom not in updated.values():
                updated[pos] = atom
        self.atoms = updated
        
    def handleCircles(self, move):
        for pos, circle in self.circles.items():
            atom1, atom2 = self.getCandidates(pos, move)
            if (atom1[1] is not None and atom2[1] is not None):
                if (circle.name == "green"):
                    self.addConnection(atom1, atom2)
                elif (circle.name == "red"):
                    print("i should handle red dots")
                    self.removeConnection(atom1, atom2)
                elif (circle.name == "blue"):
                    return           
    
    def getCandidates(self, pos, move):
        x, y = pos 
        upLeft = self.compound.get((x, y))
        upRight = self.compound.get((x + 1, y))
        downLeft = self.compound.get((x, y + 1))
        downRight = self.compound.get((x + 1, y + 1))
       
        if move == UP:
            return ((x, y + 1), downLeft), ((x + 1, y + 1), downRight)
        elif move == DOWN:
            return ((x, y), upLeft), ((x + 1, y), upRight)
        elif move == LEFT:
            return ((x + 1, y), upRight), ((x + 1, y + 1), downRight)
        return ((x, y), upLeft), ((x, y + 1), downLeft)

    def addConnection(self, atom1, atom2):
        if atom1[1].connections > 0 and atom2[1].connections > 0:
            atom1[1].connections -= 1
            atom1[1].updateImage()
            atom2[1].connections -= 1
            atom2[1].updateImage()
        
    def removeConnection(self, atom1, atom2):
        if atom1[1].canAddConnection() and atom2[1].canAddConnection():
            if atom1[1].connections == 0 and not atom1[1].isHero:
                self.compound.pop(atom1[0])
                self.atoms[atom1[0]] = atom1[1]
            elif atom2[1].connections == 0 and not atom2[1].isHero:
                self.compound.pop(atom2[0])
                self.atoms[atom2[0]] = atom2[1]
            elif atom1[1].connections == 0 and atom1[1].isHero:
                self.compound.pop(atom2[0])
                self.atoms[atom2[0]] = atom2[1]
            atom1[1].connections += 1
            atom2[1].connections += 1
            atom1[1].updateImage()
            atom2[1].updateImage()

      
    def rotateCompound(self, pos, dx, dy):
        x, y = pos 
        candidates = []
        if dx == 0 and dy == -1:
            candidates = [(x, y + 1), (x + 1, y + 1)]
        if dx == 0 and dy == 1:
            candidates = [(x, y), (x + 1, y)]
        if dx == -1 and dy == 0:
            candidates = [(x + 1, y + 1), (x + 1, y)]
        if dx == 1 and dy == 0:
            candidates = [(x, y), (x, y + 1)]
        
        l = [atom for atom in self.compound if atom.pos in candidates]

        if len(l) == 2:
            self.rotateAtom(l[1], l[0], dx, dy)
            
            
    def connectAtom(self, connection):
        atom1, (pos2, atom2) = connection
        atom1.connections -= 1
        atom1.updateImage()
        atom2.connections -= 1
        atom2.updateImage()
        self.compound[pos2] = atom2
        self.atoms.pop(pos2)

    def isNextTo(self, pos1, pos2):
        x1, y1 = pos1
        x2, y2 = pos2
        if (x1 == x2 and abs(y1 - y2) == 1): return True
        if (y1 == y2 and abs(x1 - x2) == 1): return True
        return False

    def connectAtoms(self, move):
        for atom in 
        '''for pos1, atom1 in self.compound.items():
            for pos2, atom2 in self.atoms.items():
                if self.isNextTo(pos1, pos2) and atom1.canConnectTo(atom2):
                    connections.append((atom1, (pos2, atom2)))
       
        for connection in connections:
            self.connectAtom(connection)'''
    
    def rotateAtom(self, atom1, atom2, dx, dy):
        (x1, y1) = atom1.pos
        (x2, y2) = atom2.pos
        
        if dx == 0 and dy == -1: #cima
            if (x1 < x2): 
                atom2.move(-1, 1)
            else: 
                atom1.move(-1, 1)
        if dx == 0 and dy == 1: #baixo
            if (x1 < x2): 
                atom1.move(1, -1)
            else: 
                atom2.move(1, -1)
        if dx == -1 and dy == 0: #esquerda
            if (y1 < y2): 
                atom1.move(1, 1)
            else: 
                atom2.move(1, 1)
        if dx == 1 and dy == 0: #direita
            if (y1 < y2): 
                atom2.move(-1, -1)  
            else: 
                atom1.move(-1, -1)  