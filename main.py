import igraph as ig
import matplotlib.pyplot as plt
from aStar import aStar

#interactive mode so script doesn't stall at plt.show()
plt.ion()

#open files
g1 = open("graph.txt", "r")
c1 = open("coords.txt", "r")

#set variables
n_vertices = 0
vlabels = []
edges = []
obstacles = []

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

#get the coordinates from coords file
xcoords = []
ycoords = []

for a in c1:
    newx = a.split()[1]
    newy = a.split()[2]
    xcoords.append(float(newx))
    ycoords.append(float(newy))

g1.close()
c1.close()

#create graph and vertex labels
g = ig.Graph(edges)
g.vs["name"] = vlabels
g.vs["x"] = xcoords
g.vs["y"] = ycoords
g.vs["color"] = "lightblue"
layout = ig.Layout(zip(xcoords, ycoords))

print("X coordinates:", g.vs["x"])
print("Y coordinates:", g.vs["y"])

#plot in matplotlib
fig, ax = plt.subplots(figsize=(n_vertices, n_vertices))
ig.plot(
    g,
    target=ax,
    layout=layout,
    vertex_size=30,
    vertex_label=g.vs["name"],
    vertex_coords=list(zip(g.vs["x"], g.vs["y"])),
    vertex_color=g.vs["color"],
    edge_color="gray",
)

plt.draw()
plt.pause(0.1)

print("Graph plotted successfully.")
print("Starting node: ", end="")
startingNode = input()
print("Goal node: ", end="")
goalNode = input()

g.vs.find(name=startingNode)["color"] = "green"
g.vs.find(name=goalNode)["color"] = "orange"

print("How many obstacles? ", end="")
obstacleNum = int(input())

if obstacleNum > 0:
    print("Enter obstacle ids separated by a space: ", end="")
    obstacleList = input().split()
    for obs in obstacleList:
        obstacleNode = g.vs.find(name=obs)
        obstacleNode["color"] = "red"
        obstacles.append(obs)

# Clear and redraw the graph with updated colors
ax.clear()
ig.plot(
    g,
    target=ax,
    layout=layout,
    vertex_size=30,
    vertex_label=g.vs["name"],
    vertex_coords=list(zip(g.vs["x"], g.vs["y"])),
    vertex_color=g.vs["color"],
    edge_color="gray",
)

plt.draw()
plt.pause(0.1)
print("Obstacle nodes marked in red.")

path = aStar(startingNode, goalNode, g, obstacles)
#aStar(startingNode, goalNode, plt, g, obstacles)

for i in range(len(path)-1):
    nodeA = g.vs.find(name=path[i])
    nodeB = g.vs.find(name=path[i+1])
    ax.plot(
        [nodeA["x"], nodeB["x"]],
        [nodeA["y"], nodeB["y"]],
        color="green",
        linewidth=4
    )
    plt.draw()
    plt.pause(0.5)

# Keep the script running and the plot window open
print("Press Enter to close the graph...")
input()