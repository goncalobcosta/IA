from itertools import combinations
from code.atom import *

class Compound:
    def __init__(self, atoms, isHeroCompound = False):
        self.atoms = atoms
        self.isHeroCompound = isHeroCompound
        self.visited = False
        
    def dfsDraw(self, surface, offX, offY, atom):
        """
        Perform depth-first search to draw connections between atoms in the compound.

        Parameters:
        - surface: The surface on which to draw the connections.
        - offX (int): Offset in the x-direction.
        - offY (int): Offset in the y-direction.
        - atom (Atom): The starting atom for the depth-first search.
        """
        atom.visited = True
        for neighbour in atom.connections:
            atom.drawConnection(surface, offX, offY, neighbour, atom.connections.count(neighbour))
            if not neighbour.visited:
                self.dfsDraw(surface, offX, offY, neighbour)
        
    def draw(self, surface, offX, offY):
        """
        Draw the compound on a given surface.

        Parameters:
        - surface: The surface on which to draw the compound.
        - offX (int): Offset in the x-direction.
        - offY (int): Offset in the y-direction.
        """
        for atom in self.atoms:
            atom.visited = False
        self.dfsDraw(surface, offX, offY, self.atoms[0])
        for atom in self.atoms:
            atom.draw(surface, offX, offY)
       
    def addAtom(self, atom):
        """
        Add an atom to the compound.

        Parameters:
        - atom (Atom): The atom to add to the compound.
        """
        self.atoms.append(atom)
        
    def isInPosition(self, pos):
        """
        Check if any atom in the compound is in a given position.

        Parameters:
        - pos (tuple): A tuple containing the position coordinates to check.

        Returns:
        - bool: True if any atom in the compound is in the given position, False otherwise.
        """
        return any(atom.isInPosition(pos) for atom in self.atoms)
        
    def move(self, move):
        """
        Move the compound by a given displacement.

        Parameters:
        - move (tuple): A tuple containing the displacement in the x and y directions.
        """
        for atom in self.atoms:
            atom.pos = (atom.pos[0] + move[0], atom.pos[1] + move[1])
        self.checkConnections()
            
    def connect(self, src, dest):
        """
        Connect two atoms within the compound bidirectionally.

        Parameters:
        - src (Atom): The source atom.
        - dest (Atom): The destination atom.
        """
        src.connect(dest)
        dest.connect(src) 
        
    def handleConnection(self, compound):
        """
        Handle connections between the compound and another compound.

        Parameters:
        - compound (Compound): The other compound.

        Returns:
        - list: A list of tuples containing connected atoms between the two compounds.
        """
        res = []
        for atom in self.atoms:
            for atom2 in compound.atoms:
                if atom.canConnectTo(atom2): 
                   res.append((atom, atom2))
        return res
        
    def push(self, move):
        """
        Move all atoms in the compound by a given displacement.

        Parameters:
        - move (tuple): A tuple containing the displacement in the x and y directions.
        """
        for atom in self.atoms:
            atom.move(move)
          
    def addConnection(self, atom1, atom2):
        """
        Add a connection between two atoms within the compound if their connection limits allow.

        Parameters:
        - atom1 (Atom): The first atom.
        - atom2 (Atom): The second atom.
        """
        if len(atom1.connections) < atom1.boundLimit and len(atom2.connections) < atom2.boundLimit:
            self.connect(atom1, atom2)
    
    def removeConnection(self, atom1, atom2):
        """
        Remove a connection between two atoms within the compound.

        Parameters:
        - atom1 (Atom): The first atom.
        - atom2 (Atom): The second atom.
        """
        if atom1 in atom2.connections:
            atom1.disconnect(atom2)
            atom2.disconnect(atom1)   
            
    def getCandidates(self, move, pos):
        """
        Get candidate atoms for connection based on a given move direction and position.

        Parameters:
        - move (tuple): A tuple representing the move direction.
        - pos (tuple): A tuple containing the position coordinates.

        Returns:
        - tuple: A tuple containing lists of candidate atoms for connection.
        """
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
        """
        Perform depth-first search on atoms starting from a given atom.

        Parameters:
        - atom (Atom): The starting atom for the depth-first search.
        """
        atom.visited = True
        for neighbour in atom.connections:
            if not neighbour.visited:
                self.dfs(neighbour)
    
    def checkIsolation(self):
        """
        Check for isolated atoms in the compound and remove them.

        Returns:
        - list: A list of isolated atoms.
        """
        for atom in self.atoms:
            atom.visited = False
                    
        self.dfs(self.atoms[0])
        
        isolated = [atom for atom in self.atoms if not atom.visited]
        self.atoms = [atom for atom in self.atoms if atom.visited]
        
        return isolated
    
    def reconnect(self, connections):
        """
        Reconnect atoms based on a list of connections.

        Parameters:
        - connections (list): A list of tuples containing connections between atoms.
        """
        for connection in connections:
            atom1, atom2 = connection
            self.connect(atom1, atom2)
            
    def rotate(self, move):
        """
        Rotate non-hero atoms in the compound based on a given move direction.

        Parameters:
        - move (tuple): A tuple representing the move direction.
        """
        dx, dy = move
        for i in range(len(self.atoms) - 1, 0, -1):
            atom = self.atoms[i]
            if atom.isHero: continue
            else:
                x, y = self.atoms[i-1].pos
                atom.pos = (x-dx, y-dy)
    
    def dfsSnake(self, atom, current_path):
        """
        Perform depth-first search to construct a snake-like path within the compound.

        Parameters:
        - atom (Atom): The starting atom for the depth-first search.
        - current_path (list): The current path being constructed.

        Returns:
        - list: The snake-like path within the compound.
        """
        atom.visited = True
        current_path.append(atom)

        for a in atom.connections:
            if not a.visited:
                self.dfsSnake(a, current_path)
                break

        return current_path

    def isSnake(self):
        """
        Check if the compound forms a snake-like path.

        Returns:
        - bool: True if the compound forms a snake-like path, False otherwise.
        """
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
        """
        Check and establish connections between atoms within the compound.
        """
        for atom1, atom2 in combinations(self.atoms, 2):
            if(atom1.canConnectTo(atom2) and (atom2 not in atom1.connections)):
                self.connect(atom1,atom2)

    def fullyConnected(self):
        """
        Check if all atoms in the compound are fully connected.

        Returns:
        - bool: True if all atoms are fully connected, False otherwise.
        """
        for atom in self.atoms:
            if len(atom.connections) < atom.boundLimit:
                return False
        return True
    
    def distance(self, other):
        """
        Calculate the minimum Manhattan distance between this compound and another compound.

        Parameters:
        - other (Compound): The other compound.

        Returns:
        - float: The minimum Manhattan distance between the two compounds.
        """
        distance = float('inf')
        for atom in self.atoms:
            for elem in other.atoms:
                d = atom.manhattanDistance(elem)
                if (d < distance):
                    distance = d
        return distance
    
    def __eq__(self, other):
        """
        Compare two compounds for equality.

        Parameters:
        - other (Compound): The other compound to compare with.

        Returns:
        - bool: True if the compounds are equal, False otherwise.
        """
        if isinstance(other, self.__class__):
            return (self.atoms == other.atoms)
        else:
            return False
    
    def copy(self):
        """
        Create a copy of the compound.

        Returns:
        - Compound: A copy of the compound.
        """
        atoms = []
        for atom in self.atoms:
            atoms.append(Atom((atom.name, atom.boundLimit), atom.pos, atom.isHero))

        for i, atom in enumerate(self.atoms):
            connections = [self.atoms.index(con) for con in atom.connections]
            for j in connections:
                atoms[i].connections.append(atoms[j])

        compound = self.__class__(atoms, self.isHeroCompound)
        return compound
    
    def __hash__(self):
        return hash((tuple(atom for atom in self.atoms), self.isHeroCompound))