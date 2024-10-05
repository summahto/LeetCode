class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        pq = []
        dist = [float('inf') for i in range(n+1)]
        visited = [False] * (n+1)

        source = k

        adj = {}
        for i in range(1, n+1):
            adj[i] = []
        
        for (u, v, w) in times:
            adj[u].append((v, w))

        # print(adj)
        
        dist[source] = 0
        pq.append((0, source))

        # print(dist)

        while pq:
            (currDist, currNode) = heapq.heappop(pq)

            if visited[currNode]:
                continue
            
            visited[currNode] = True

            for (v, w) in adj[currNode]:
                vDist = currDist + w

                if vDist < dist[v]:
                    dist[v] = vDist
                    heapq.heappush(pq, (dist[v], v))

        
        # print(dist)
        ans = 0
        for i in range(1, n+1):
            if dist[i] == float('inf'):
                return -1
            else :
                ans = max(ans, dist[i])

        return ans