from node import Node
from graph import Graph
from random import randint

if __name__ == "__main__":
    GR = Graph()
    numberOfGraphs = randint(1,10)
    GR.populateGraph(numberOfGraphs)
    print(GR.size)
    GR.defineNeighbors