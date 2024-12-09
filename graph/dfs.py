from typing import List, Dict


def dfs(adj: dict[List[int]], u:int, visited: List[bool], ans: List[int]):

    if visited[u] is True:
        return

    visited[u] = True
    ans.append(u)
    for v in adj[u]:
        if not visited[v]:
            dfs(adj, v, visited, ans)


if __name__ == '__main__':
    # [a, b] -> must take b first, b is a pre-requisite of a
    # b --- > a
    n = 4
    pre = [[1, 0], [2, 0], [2, 1], [3, 1]]

    adj = dict()

    for i in range(n):
        adj[i] = []

    for row in pre:
        u = row[1]
        v = row[0]

        adj[u].append(v)

    print(adj)

    visited: List[bool] = [False] * 4

    print(visited)
    ans = []
    dfs(adj, 0, visited, ans)

    print(ans)


