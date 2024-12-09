from typing import List, Deque
from collections import deque

def bfs(adj: dict[List[int]], u:int, queue: Deque[tuple[int, int]], visited: list[bool]):
    queue.append((u, -1))

    while queue:
        (u, parent) = queue.popleft()
        visited[u] = True

        for v in adj[u]:

            if v == parent:
                continue

            if visited[v]:
                return True

            queue.append((v, u))

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
    queue: Deque = deque()

    visited: List[bool] = [False] * n

    for i in range(n):
        if not visited[i]:
            if bfs(adj, i, queue, visited):
                print(i, "has cycle")
                has_cycle = True


    print(has_cycle)
