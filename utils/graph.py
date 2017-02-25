import networkx
from networkx import MultiDiGraph
from datetime import datetime
from random import randint

name = 'name'
weigth = 'weigth'

terrain1 = {name : 'grass', weigth : 2}
terrain2 = {name : 'mountain', weigth : 3}
terrain3 = {name : 'grass1', weigth : 2}
terrain4 = {name : 'mountain1', weigth : 3}

g = MultiDiGraph()

for i in range(1000):
    if i > 0:
        g.add_edge(i-1, i, weight=1)
        g.add_edge(i, i-1, weight=1)
    else:
        g.add_edge(terrain4[name], i, weight=1)
        g.add_edge(i, terrain4[name], weight=1)
    if i < 1000:
        g.add_edge(i, i+1, weight=1)
        g.add_edge(i+1, i, weight=1)
    rand = randint(1,1000)
    g.add_edge(i, rand, weight=1)
    g.add_edge(rand, i, weight=1)

g.add_edge(terrain1[name], terrain2[name], weight=terrain2[weigth])
g.add_edge(terrain2[name], terrain1[name], weight=terrain1[weigth])
g.add_edge(terrain2[name], terrain3[name], weight=terrain3[weigth])
g.add_edge(terrain3[name], terrain4[name], weight=terrain4[weigth])
g.add_edge(terrain4[name], terrain3[name], weight=terrain3[weigth])

start = datetime.now()
print(networkx.single_source_dijkstra_path_length(g, terrain1[name], cutoff=3))
end = datetime.now()
print("Duration: {}".format(end-start))

start = datetime.now()
print(networkx.single_source_dijkstra_path_length(g, terrain1[name], cutoff=10))
end = datetime.now()
print("Duration: {}".format(end-start))

start = datetime.now()
print(networkx.single_source_dijkstra_path_length(g, 0, cutoff=10))
end = datetime.now()
print("Duration: {}".format(end-start))

start = datetime.now()
print(networkx.single_source_dijkstra_path_length(g, 1000, cutoff=10))
end = datetime.now()
print("Duration: {}".format(end-start))

start = datetime.now()
print(networkx.dijkstra_path(g, 0, 1000))
end = datetime.now()
print("Duration: {}".format(end-start))

