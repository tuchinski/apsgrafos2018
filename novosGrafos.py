import networkx as nx

g = nx.Graph()

g.add_node(1)
g.add_node(2)
g.add_node(3)
g.add_node(4)
g.add_node(5)
g.add_node(6)

g.add_edge(1,2,weight=4)
g.add_edge(1,3,weight=2)
g.add_edge(2,3,weight=1)
g.add_edge(2,4,weight=5)
g.add_edge(3,4,weight=8)
g.add_edge(3,5,weight=10)
g.add_edge(4,5,weight=2)
g.add_edge(4,6,weight=6)
g.add_edge(5,6,weight=2)

pred, dist = nx.dijkstra_predecessor_and_distance(g,1)

print("Predecessor:")
print(pred)

print("distancia:")
print(dist)

