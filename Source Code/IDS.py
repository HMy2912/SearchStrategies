maxDepth = 40


def DLS(graph, path, goal, depth, expanded):
    node = path[-1]

    if node == goal:
        return path

    if depth <= 0:
        return None

    for child in range(len(graph[node])):
        if graph[node][child] != 0:
            if child not in path:
                expanded.append(child)
                new_path = path.copy()
                new_path.append(child)
                next_path = DLS(graph, new_path, goal, depth - 1, expanded)
                if next_path is not None:
                    return next_path


def IDS_Algorithm(graph, start, goal):
    expandedSet = []
    expanded = []
    for i in range(maxDepth):
        expanded.clear()
        expanded.append(start)
        path = DLS(graph, [start], goal, i, expanded)
        if expanded not in expandedSet:
            expandedSet.append(expanded.copy())
        if path is None:
            continue
        return expandedSet, path
    return expandedSet, None
