from node import Node
from random import randint

class Graph:
    def __init__(self):
        self.size = 0
        self.nodes = []
        self.colors = ["red", "blue", "green", "yellow", "gray"]
        
    def getColors(self):
        return self.colors
    
    def addNode(self, node):
        if(len(self.nodes)>9):
            return False
        self.nodes.append(node)
        
    def populateGraph(self, size):
        self.size = size
        for x in range(0, size):
            ND = Node()
            self.nodes.append(ND)
            
    def defineNeighbors(self,nodes):
        for node in nodes:
            numberOfNeighbors = randint(1,5)
            for x in range(0,numberOfNeighbors):
                if len(node.neighbors) is 0:
                    #Precisa criar o algorítimo para popular os vizinhos
                    node.addNeighbor(nodes[x])