class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        
        n = len(isConnected)
        visited = [False] * n
        count = 0

        def bfs():

            while q:
                u = q.popleft()
                visited[u] = True

                for v in range(n):
                    if not visited[v] and isConnected[u][v] == 1:
                        q.append(v)

        q = deque()

        for i in range(n):
            if not visited[i]:
                q.append(i)
                bfs()
                count += 1

        return count





