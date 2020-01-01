#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Maximum flow by Ford-Fulkerson
Complexity O(|V|*|E|*max_capacity)
"""


def add_reverse_arcs(graph):
    for u in list(graph.keys()):
        for v in graph[u]:
            if u not in graph[v]:
                graph[v][u] = 0


def _augment(graph, flow, val, u, target, visit):
    """Find an augmenting path from u to target with value at most val"""
    visit[u] = True
    if u == target:
        return val
    for v in graph[u]:
        if not visit[v] and graph[u][v] > flow[u][v]:
            res = min(val, graph[u][v] - flow[u][v])
            delta = _augment(graph, flow, res, v, target, visit)
            if delta > 0:
                flow[u][v] += delta
                flow[v][u] -= delta
                return delta
    return 0


def ford_fulkerson(graph, s, t, matrix_output=False):
    """Maximum flow by Ford-Fulkerson
    :param graph: weighted directed graph in defaultdict(dict) format
    :param int s: source vertex
    :param int t: target vertex
    :param bool matrix_output: either output a dict(dict) flox of a matrix
    :returns: flow output, flow value
    :complexity: `O(|V|*|E|*max_capacity)`
    """
    add_reverse_arcs(graph)
    n = len(graph)

    if matrix_output:
        flow = [[0] * n for _ in range(n)]
    else:
        flow = {u: {v: 0 for v in graph[u]} for u in graph}

    while _augment(graph, flow, float('inf'), s, t, [False]*n)>0:
        pass

    return (flow, sum(flow[s] if type(flow) is list else flow[s].values()))