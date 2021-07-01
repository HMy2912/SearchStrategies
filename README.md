# SearchStrategies
A program to find an (optimal) path from the source node to the destination node on a graph, using either of the following strategies: • Breadth-first search (BFS) • Tree-search depth-first search (DFS) • Uniform-cost search (UCS) • Iterative deepening search (IDS) • Greedy best first search (GBFS) • Graph-search A* (A Star) • Hill-climbing (HC)

## General Description
### Input file
The first line is the number of nodes in the graph (n).
The second line is included three integer, respectively the start node, the goal node and the number of the algorithm to be used.
* 0: BFS
* 1: DFS
* 2: UCS
* 3: IDS
* 4: GBFS
* 5: A Star
* 6: HC

The next n lines are the adjency matrix of the graph.
The last line is the list of heuristic of the graph.

### Output file
The first line is the list of node expanded during the searching.
The second line is the path that found with the algorithm. If there is no path, the 'No path.' is printed.

## Document
### Report
First section is 3 different graphs in each algorithm and its result, also the input and output file.
Second section is about giving comments in the average number of nodes based on the properties or characteristics of each algorithm.
Thirs section is the references used in the process of making this.

Please give a citation, if you get any references from this.
