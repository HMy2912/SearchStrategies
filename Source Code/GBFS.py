from queue import PriorityQueue


def GBFS_Algorithm(graph, heu, start, goal):
    frontier = PriorityQueue()
    expanded = []
    path = []
    path.append(start)
    frontier.put((heu[start], path))

    while frontier and not frontier.empty():
        heuristic, node = frontier.get()
        current = node[-1]
        if current not in expanded:
            if current == goal:
                return expanded, node
            expanded.append(current)

            for neighbor in range(len(graph[current])):
                if neighbor not in expanded and graph[current][neighbor] != 0:
                    totalHeu = heu[neighbor]
                    path = node.copy()
                    path.append(neighbor)
                    frontier.put((totalHeu, path))
    return expanded, None
