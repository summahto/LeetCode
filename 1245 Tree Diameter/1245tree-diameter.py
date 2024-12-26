class Solution:
    def treeDiameter(self, edges: List[List[int]]) -> int:
        
        # if we take any node and find the farthest leaf node from this node, it is guaranteed to be one of the ends of the diameter
        # lets implement this using BFS

        # make an adjacency list first

        adj = defaultdict(list)

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        q = deque()
        q.append(0)
        level = -1
        dist = -1

        farthestNode = 0
        visited = set()
        while q:
            n = len(q)
            level += 1
            dist += 1

            while n >0:
                u = q.popleft()
                # as you pop out an element set it as the farthest node
                farthestNode = u

                for v in adj[u]:
                    if v not in visited:
                        q.append(v)
                        visited.add(u)

                n-= 1

        # print(f"{farthestNode=}")
        # print(f"{dist=}")

        # now from the farthest node found look for the most distant node from here
        diameterEnd = farthestNode
        q.append(farthestNode)

        dist = -1
        level = -1
        visited = set()

        while q:
            n = len(q)
            dist+= 1
            level +=1 
            while n > 0:
                u = q.popleft()
                farthestNode = u
                
                for v in adj[u]:
                    if v not in visited:
                        q.append(v)
                        visited.add(u)

                n-=1
        
        # print(f"{farthestNode=}")
        # print(f"{dist=}")

        return dist




