def __findPathDFS(graph, current, goal, visited, expanded):
    expanded.append(current)
    if current == goal:
        return [current]
    for neighbor in range(0, len(graph[current])):
        if graph[current][neighbor] != 0:
            if neighbor not in visited:
                visited.add(neighbor)
                path = __findPathDFS(graph, neighbor, goal, visited, expanded)

                if path is not None:
                    path.insert(0, current)
                    return path
    return None


def DFS_Algorithm(graph, start, goal):
    expanded = []
    visited = set()
    if start < 0 or goal > len(graph):
        return False

    visited.add(start)

    result = __findPathDFS(graph, start, goal, visited, expanded)
    return expanded, result
