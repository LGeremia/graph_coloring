class Node:
    neighbors = []
    def __init__(self):
        self.color = None
        
    def setColor(self,color):
        if(self.color is not None):
            return False
        self.color = color
        
    def addNeighbor(self,neighbor):
        if(len(self.neighbors)>4):
            return False
        self.neighbors.append(neighbor)
        
    def getColor(self):
        return self.color
    
    def getNeighbors(self):
        return self.neighbors