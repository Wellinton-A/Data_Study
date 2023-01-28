class Graph:
    def __init__(self):
        self.numberOfNodes = 0
        self.graph = dict()
    
    def add_vertex(self, node):
        self.graph.update({node: list()})
    
    def add_edge(self, node, conec):
        self.graph[node].append(conec)
        if conec in self.graph:
            self.graph[conec].append(node)


myGraph = Graph()
myGraph.add_vertex(0)
myGraph.add_vertex(1)
myGraph.add_vertex(2)
myGraph.add_vertex(3)
myGraph.add_vertex(4)
myGraph.add_vertex(5)
myGraph.add_vertex(6)
myGraph.add_edge(3, 1)
myGraph.add_edge(3, 4)
myGraph.add_edge(4, 2)
myGraph.add_edge(4, 5)
myGraph.add_edge(1, 2)
myGraph.add_edge(1, 0)
myGraph.add_edge(0, 2)
myGraph.add_edge(6, 5)

print(myGraph.graph)
    
