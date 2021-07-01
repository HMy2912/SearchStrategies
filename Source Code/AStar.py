from queue import PriorityQueue


def AStar_Algorithm(graph, heu, start, goal):
    expanded = []
    path = []
    parents = {}
    frontier = PriorityQueue()
    frontier.put((0, start, None))

    while frontier and not frontier.empty():
        cost, node, par = frontier.get()
        if node not in expanded:
            expanded.append(node)
            parents[node] = par

            if node is goal:
                while parents[node] is not None:
                    path.append(node)
                    node = parents[node]
                path.append(start)
                return expanded, path[::-1]

            for child in range(len(graph[node])):
                if child not in expanded and graph[node][child] != 0:
                    gChild = cost + graph[node][child]
                    hChild = heu[child]
                    fChild = gChild + hChild - heu[node]
                    frontier.put((fChild, child, node))
    return expanded, None
