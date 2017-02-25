'''
Node = (LABEL,)
Edge = cost->

dijkstra_path search from the shortest path between source and destiny
it can be used with only a source to give all the shortest path reachable by source
it also can receive a cutoff to calculate the paths with max_weight=cutoff

In a cenary like this:

(A, my_troop) 1-> (B,enemy)
    |               |
    |               |1-> (D,)
    |               |
    |               |1-> (E,)
    |               |
    |               |1-> (C,)
    |                      ^
    |1->(F,)--1->(G,)-----1|

Enemies are obstacles to allies, so shortest paths cannot be calculated passing by nodes with enemies

The valid moviments of my_troop with only dijkstra_path will be:
{'A': 0, 'B': 1, 'C': 2, 'D': 2, 'E': 2, 'F': 1, 'G': 2}

But we expect:
{'A': 0, 'B': 1, 'C': 3, 'F': 1, 'G': 2}

So, how can we get the expected result?
    #1 We need to get the first dijkstra_path result
    #2 See what nodes have troops
    #3 Pass the nodes with troops and it costs to our container with final_valid_moviments
    #4 Get a subgraph with all the dijkstra_path nodes from the original graph | The execution of dijkstra_path in a subgraph is at least 3x better than a copy of the original graph, and occupy less memory
    #5 Delete the nodes with troops
    #6 Calculate the new dijkstra_paths
    #7 Merge the new dijkstra_paths with the final_valid_moviments

'''


import networkx
from networkx import MultiDiGraph
from datetime import datetime

default_weight = 1

A = 'A'
B = 'B'
C = 'C'
D = 'D'
E = 'E'
F = 'F'
G = 'G'

g = MultiDiGraph()
g.add_edge(A, B, weight=default_weight)
g.add_edge(A, F, weight=default_weight)
g.add_edge(B, C, weight=default_weight)
g.add_edge(B, D, weight=default_weight)
g.add_edge(B, E, weight=default_weight)
g.add_edge(F, G, weight=default_weight)
g.add_edge(G, C, weight=default_weight)


final_valid_moviments = {}

#1
start = datetime.now()
dijkstra = networkx.single_source_dijkstra_path_length(g, A)
print(dijkstra)

#2 We assume that we already see that B have an obstacle
OBSTACLE = B

#3
final_valid_moviments[OBSTACLE] = dijkstra[OBSTACLE]

#4
gsub = g.subgraph(dijkstra.keys())

#5
gsub.remove_node(OBSTACLE)

#6
dijkstra = networkx.single_source_dijkstra_path_length(gsub, A)

#7
final_valid_moviments.update(dijkstra)
print(final_valid_moviments)
end = datetime.now()
print("Duration: {}".format(end-start))