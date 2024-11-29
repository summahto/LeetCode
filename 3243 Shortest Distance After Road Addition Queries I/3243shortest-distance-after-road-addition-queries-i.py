from collections import deque

class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        
        # initial distance array
        d = [ i for i in range(n)]

        ans = []
        adj = {}
        for u in range(n):
            adj[u] = []
        
        for i in range(n):
            adj[i].append(i+1)
        
        # print(f"{adj=}")

        def bfs(adj, q, visited):
            level = 0
            visited[0] = True

            while q:
                q_length = len(q)
                # print(f"{q=}")

                while q_length > 0:
                    (curr) = q.popleft()
                    
                    
                    if curr == n-1:
                        return level
                    

                    for v in adj[curr]:
                        if not visited[v]:
                            # print(f"{curr=} {v=}")
                            q.append(v)
                            visited[v]= True

                    q_length -= 1
                
                level += 1

            return 0


        # find the shortest path from 0 to n-1 after each query
        for q in queries:
            u = q[0]
            v = q[1]
            
            adj[u].append(v)

            # find shortest path after adding a new route, now
            q = deque()
            # each element (node, path_length)
            q.append(0)
            visited = [False]* n

            # since there are no weights, BFS gives the shortest Path
            shortest_path = bfs(adj, q, visited)

            ans.append(shortest_path)

            
        return ans