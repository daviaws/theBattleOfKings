import networkx
from networkx import MultiDiGraph

default_weigth = 1

nodes = {
    'A':{
            'adjacents': ['B', 'C'],
            'weight': 1
        },
    'B':{
            'adjacents': ['A', 'D'],
            'weight': 2
        },
    'C':{
            'adjacents': ['A', 'D'],
            'weight': 1
        },
    'D':{
            'adjacents': ['B', 'C'],
            'weight': 1
        }

}
g = MultiDiGraph()

for src, attr in nodes.items():
    for dst in attr['adjacents']:
        weight = nodes[dst]['weight']
        g.add_edge(src, dst, weight=weight)

print(g.edges())