from typing import List, Dict


def dfs(adj, u, visited, parent):

    visited[u] = True

    for v in adj[u]:
        if parent == v:
            continue
        if visited[v]:
            return True

        if dfs(adj, v, visited, u):
            return True

    return False




if __name__ == '__main__':
    # [a, b] -> must take b first, b is a pre-requisite of a
    # b --- > a
    n = 5
    # pre = [[0, 1], [1, 0], [1, 2], [1, 4], [2, 1], [2, 3], [3, 2], [3, 4], [4, 3], [4, 1]]
    pre = [[0, 1], [1, 0]]

    adj = dict()

    for i in range(n):
        adj[i] = []

    for row in pre:
        u = row[0]
        v = row[1]

        adj[u].append(v)

    print(adj)

    has_cycle = False

    for i in range(n):

        visited: List[bool] = [False] * n

        if dfs(adj, i, visited, -1):
            print(i, "has cycle")
            has_cycle = True

        else:
            print(i, "no cycle")

    print(has_cycle)