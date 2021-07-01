from queue import PriorityQueue


def UCS_Algorithm(graph, start, goal):
    frontier = PriorityQueue()
    expanded = []
    path = []
    path.append(start)
    frontier.put((0, path))

    while frontier and not frontier.empty():
        cost, node = frontier.get()
        current = node[-1]
        if current not in expanded:
            expanded.append(current)

            if current == goal:
                return expanded, node

            for neighbor in range(len(graph[current])):
                if neighbor not in expanded and graph[current][neighbor] != 0:
                    totalCost = cost + graph[current][neighbor]
                    path = node.copy()
                    path.append(neighbor)
                    frontier.put((totalCost, path))
    return expanded, None
