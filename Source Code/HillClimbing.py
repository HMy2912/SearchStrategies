import random


def HC(graph, heu, start, goal, visited):
    visited.append(start)
    children = []
    for child in range(len(graph[start])):
        if graph[start][child] != 0 and child not in visited and heu[child] <= heu[start]:
            children.append(child)

    if len(children) > 0:
        HC(graph, heu, random.choice(children), goal, visited)

    return visited


def HillClimbing_Algorithm(graph, heu, start, goal):
    visited = []
    expanded = HC(graph, heu, start, goal, visited)
    if goal not in expanded:
        path = None
    else:
        path = expanded.copy()
    return expanded, path
