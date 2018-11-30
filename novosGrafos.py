import networkx as nx
import matplotlib.pyplot as plt

g = nx.Graph()

# g.add_node(1)
# g.add_node(2)
# g.add_node(3)
# g.add_node(4)
# g.add_node(5)
# g.add_node(6)

# g.add_edge(1,2,weight=4)
# g.add_edge(1,3,weight=2)
# g.add_edge(2,3,weight=1)
# g.add_edge(2,4,weight=5)
# g.add_edge(3,4,weight=8)
# g.add_edge(3,5,weight=10)
# g.add_edge(4,5,weight=2)
# g.add_edge(4,6,weight=6)
# g.add_edge(5,6,weight=2)

g.add_nodes_from([0,1,2,3])

g.add_edge(0,1,weight=10)
g.add_edge(0,2,weight=64)
g.add_edge(0,3,weight=56)
g.add_edge(1,3,weight=5)
g.add_edge(1,2,weight=23)
g.add_edge(3,2,weight=37)

# pred, dist = nx.dijkstra_predecessor_and_distance(g,1)
di = nx.minimum_spanning_tree(g)

# plt.subplot(121)
nx.draw(di, with_labels = True, font_weight="bold")
plt.show()

# print("Predecessor:")
# print(pred)

# print("distancia:")
# print(dist)

print(di.edges)