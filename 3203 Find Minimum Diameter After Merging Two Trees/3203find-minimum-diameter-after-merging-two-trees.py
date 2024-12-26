class Solution:
    def minimumDiameterAfterMerge(self, edges1: List[List[int]], edges2: List[List[int]]) -> int:
        

        def findFarthestNode(adj, source):
            
            q = deque()
            q.append(source)
            
            farthestNode = source
            level = -1
            dist = -1

            visited = set()
            
            while q:
                n = len(q)
                level += 1
                dist += 1

                while n > 0:
                    u = q.popleft()
                    farthestNode = u
                    visited.add(u)

                    for v in adj[u]:
                        if v not in visited:
                            q.append(v)
                            visited.add(v)

                    n -= 1
                
            return dist, farthestNode
        

        def formAdjList(edges):
            n = len(edges) + 1
            
            adj = defaultdict(list)

            for u, v in edges:
                adj[u].append(v)
                adj[v].append(u)

            return adj
        
        adj1 = formAdjList(edges1)
        adj2 = formAdjList(edges2)

        distG1, g1End1 = findFarthestNode(adj1, 0)
        distG2, g2End1 = findFarthestNode(adj2, 0)

        diameter1, g1End2 = findFarthestNode(adj1, g1End1)
        diameter2, g2End2 = findFarthestNode(adj2, g2End1)
        
        # print(f"{diameter1=} {g1End1=} {g1End2=} {distG1=}")
        # print(f"{diameter2=} {g2End1=} {g2End2=} {distG2=}")

        return max((ceil(diameter1/2) + ceil(diameter2/2) + 1), diameter1, diameter2)

         
