from .ford_fulkerson import ford_fulkerson, add_reverse_arcs
from collections import defaultdict


def test_basic():
    graph = defaultdict(dict)
    graph[0][1] = 7
    graph[0][2] = 8
    graph[1][2] = 2
    graph[1][5] = 5
    graph[2][4] = 10
    graph[3][4] = 2
    graph[3][5] = 3
    graph[4][5] = 12

    assert ford_fulkerson(graph, 0, 5, matrix_output=True) == ([[0, 7, 8, 0, 0, 0], [-7, 0, 2, 0, 0, 5], [-8, -2, 0, 0, 10, 0], [
        0, 0, 0, 0, 0, 0], [0, 0, -10, 0, 0, 10], [0, -5, 0, 0, -10, 0]], 15)

    assert ford_fulkerson(graph, 0, 5, matrix_output=False) == ({0: {1: 7, 2: 8}, 1: {2: 2, 5: 5, 0: -7}, 2: {
        4: 10, 0: -8, 1: -2}, 3: {4: 0, 5: 0}, 4: {5: 10, 2: -10, 3: 0}, 5: {1: -5, 3: 0, 4: -10}}, 15)