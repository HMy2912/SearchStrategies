from BFS import BFS_Algorithm
from DFS import DFS_Algorithm
from UCS import UCS_Algorithm
from IDS import IDS_Algorithm
from GBFS import GBFS_Algorithm
from AStar import AStar_Algorithm
from HillClimbing import HillClimbing_Algorithm
from itertools import chain


def main():
    # Read The File
    with open('input_RP_2.txt', 'r') as f:
        readLines = f.readlines()
        lines = [line[:-1] for line in readLines if line[-1] == '\n']
        lines.append(readLines[-1])
        f.close()

    # Change from string to int && Graph
    vertices = int(lines[0])
    line2 = list(lines[1].split(" "))
    startVertex = int(line2[0])
    goalVertex = int(line2[1])
    typeAlgo = int(line2[-1])
    Graph = []
    for i in range(vertices):
        Graph.append(list(lines[i + 2].split(" ")))
    Graph = [list(map(int, _)) for _ in Graph]
    Heuristic = list(lines[-1].split(" "))
    Heuristic = list(map(int, Heuristic))

    # Print out to check
    # print(Graph)

    # Check Isolated Vertex for start and goal
    def checkIsolatedStartGoal(Graph, node):
        for child in range(len(Graph[node])):
            if Graph[node][child] != 0:
                return False
        return True

    if checkIsolatedStartGoal(Graph, startVertex):
        return None, None

    if typeAlgo == 0:
        expanded, result = BFS_Algorithm(Graph, startVertex, goalVertex)
    elif typeAlgo == 1:
        expanded, result = DFS_Algorithm(Graph, startVertex, goalVertex)
    elif typeAlgo == 2:
        expanded, result = UCS_Algorithm(Graph, startVertex, goalVertex)
    elif typeAlgo == 3:
        expanded, result = IDS_Algorithm(Graph, startVertex, goalVertex)
        expanded = list(chain.from_iterable(expanded))
    elif typeAlgo == 4:
        expanded, result = GBFS_Algorithm(
            Graph, Heuristic, startVertex, goalVertex)
    elif typeAlgo == 5:
        expanded, result = AStar_Algorithm(
            Graph, Heuristic, startVertex, goalVertex)
    elif typeAlgo == 6:
        expanded, result = HillClimbing_Algorithm(
            Graph, Heuristic, startVertex, goalVertex)

    # Print the Result to check
    print(expanded)
    print(result)

    # convert lists && no path
    expandedStr = ' '.join(map(str, expanded))
    if result is not None:
        pathStr = ' '.join(map(str, result))
    else:
        pathStr = 'No path.'

    # Write to file output.txt
    with open('output.txt', 'w') as file:
        file.write(expandedStr)
        file.write('\n')
        file.write(pathStr)
        file.close()


main()
