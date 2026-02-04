import math

def aStar(start, goal, plot, graph, obstacles):
    print(f"Running A* algorithm from {start} to {goal}...")
    open = []
    closed = []
    path = []
    currentNode = graph.vs.find(name=start)
    goalNode = graph.vs.find(name=goal)

    s2g_dist = math.dist((currentNode["x"], currentNode["y"]), (goalNode["x"], goalNode["y"]))
    print(s2g_dist)
    print(graph)
    # Placeholder for A* algorithm implementation
    # This function would contain the logic to perform the A* search
    # and return the path from start to goal.



    #look at first node
    #calculate straight line distance to goal
    #look at neighbors
    #calculate f(n) = g(n) + h(n)
    #this means calculate cost of neighbors to goal plus cost to get to neighbor
    #choose neighbor with lowest f(n)
    #repeat until goal is reached

    return path
    