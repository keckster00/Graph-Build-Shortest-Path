# Graph-Build-Shortest-Path

Libraries needed (if not installed)
igraph
matplotlib.pyplot
math
heapq

How to run:

1. Add graph.txt and coords.txt files to folder
2. Run the main.py file
3. The graph will show up
4. The command line will ask you for a start node, then goal node
5. The command line will then ask you for a number of obstacles
6. If there are obstacles, input the exact number of obstacles, and then the index numbers of the nodes separated by a space
7. Watch the program run!

The graph.txt file is a list of integers for the nodes and their neighbor nodes

1 2 3 5

2 1 4

3 1 4 5

4 2 3 

5 1 3

(Ie. 1 is connected to 2, 3 and 5, 2 is connected to 1 and 4 etc.)


The coords.txt file is the x and y coordinates of each node

1 1.50 2.54

2 3.2 3.33

3 1.3 0.0

