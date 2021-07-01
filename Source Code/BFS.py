# finds shortest path between 2 nodes of a graph using BFS
def BFS_Algorithm(graph, start, goal):
    # keep track of explored nodes
    explored = []
    # keep track of all the paths to be checked
    queue = [[start]]
    expanded = []
    expanded.append(start)
    # return path if start is goal
    if start == goal:
        return expanded, [start]

    # keeps looping until all possible paths have been checked
    while queue:
        # pop the first path from the queue
        path = queue.pop(0)
        # get the last node from the path
        node = path[-1]
        if node not in expanded:
            expanded.append(node)

        if node not in explored:
            # go through all neighbour nodes, construct a new path and
            # push it into the queue
            for neighbour in range(len(graph[node])):
                if graph[node][neighbour] != 0:
                    new_path = list(path)
                    new_path.append(neighbour)

                    queue.append(new_path)
                    # return path if neighbour is goal
                    if neighbour == goal:
                        # print(queue)
                        return expanded, new_path
            # mark node as explored
            explored.append(node)

    # in case there's no path between the 2 nodes
    return expanded, None
