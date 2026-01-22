import igraph as ig
import matplotlib.pyplot as plt

#open files
g1 = open("graph.txt", "r")
c1 = open("coords.txt", "r")

#set variables
n_vertices = 0
vlabels = []
edges = []

#for each line in graph file, create vertices and edges
#if an edge already exists, do not add it again
for x in g1:
    n_vertices += 1
    vlabels.append(x.split()[0])
    for y in x.split()[1:]:
        newEdge = (n_vertices - 1, int(y)-1)
        if (newEdge[1], newEdge[0]) not in edges:
            edges.append(newEdge)
    
print("Number of vertices:", n_vertices)
print("Vertex labels:", vlabels)
print("Edges:", edges)

#create graph and vertex labels
g = ig.Graph(edges)
g.vs["name"] = vlabels
g.vs["x"] = []
g.vs["y"] = []

for x in c1:
    g.vs["x"].append(float(x.split()[1]))
    g.vs["y"].append(float(x.split()[2]))

print("X coordinates:", g.vs["x"])
print("Y coordinates:", g.vs["y"])

#plot in matplotlib
fig, ax = plt.subplots(figsize=(n_vertices, n_vertices))
ig.plot(
    g,
    target=ax,
    layout="circle",
    vertex_size=30,
    vertex_label=g.vs["name"],
    vertex_color="lightblue",
    edge_color="gray",
)

plt.show()
