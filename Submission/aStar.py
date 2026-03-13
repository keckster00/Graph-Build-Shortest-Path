import math
from heapq import heappush, heappop

def aStar(start, goal, graph, obstacles):
    print(f"Running A* algorithm from {start} to {goal}...")

    currentNode = graph.vs.find(name=start)
    goalNode = graph.vs.find(name=goal)

    #look at first node
    #calculate straight line distance to goal
    #look at neighbors
    #calculate f(n) = g(n) + h(n)
    #this means calculate cost of neighbors to goal plus cost to get to neighbor
    #choose neighbor with lowest f(n)
    #repeat until goal is reached

    open = []
    closed = []
    
    heappush(open, (0, currentNode.index))
    
    #list of distances from start to each node
    gScore = {v.index: float('inf') for v in graph.vs}
    gScore[currentNode.index] = 0
    
    #parent nodes list
    parents = {}
    
    while open:
        #node with lowest f from priority queue (ignore priority value)
        _, currentIndex = heappop(open)
        current = graph.vs[currentIndex]
        
        #is goal?
        if current.index == goalNode.index:
            #get path through parents
            path = []
            nodeIndex = current.index
            while nodeIndex in parents:
                path.append(graph.vs[nodeIndex]["name"])
                nodeIndex = parents[nodeIndex]
            path.append(start)
            path.reverse()
            print(f"Path found: {' -> '.join(path)}")
            return path
        
        #if processed
        if current.index in closed:
            continue
        
        #else add to closed    
        closed.append(current.index)
        
        #grab neighbors
        neighbors = graph.neighbors(current.index)
        
        for neighborIndex in neighbors:
            neighbor = graph.vs[neighborIndex]
            
            #skip obstacles
            if neighbor["name"] in obstacles:
                continue
                
            #skip processed
            if neighborIndex in closed:
                continue
            
            #get g
            cost = math.dist(
                (current["x"], current["y"]),
                (neighbor["x"], neighbor["y"])
            )
            maybeG = gScore[current.index] + cost
            
            #check if shortest
            if maybeG < gScore[neighborIndex]:
                parents[neighborIndex] = current.index
                gScore[neighborIndex] = maybeG
                
                #get h
                hScore = math.dist(
                    (neighbor["x"], neighbor["y"]),
                    (goalNode["x"], goalNode["y"])
                )
                f = maybeG + hScore
                
                #add to open
                heappush(open, (f, neighborIndex))
        
    print("No path found!")
    return None
    