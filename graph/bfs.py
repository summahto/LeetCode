from typing import List, Deque
from collections import deque


def bfs(adj, u, visited, ans):

    q: Deque[int] = deque()

    q.append(u)
    visited[u] = True

    while q:
        u = q.popleft()
        ans.append(u)

        for v in adj[u]:
            if not visited[v]:
                q.append(v)
                visited[v] = True


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

    queue = deque()
    queue.append(0)

    visited : bool = [False] * n

    ans = []
    bfs(adj, 0, visited, ans)

    print(ans)
