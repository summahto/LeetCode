class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        
        n = len(graph)

        if n < 3:
            return True

        color = [-1] * n
        q = deque()

        def bfs(curr, currColor):
            color[curr] = currColor
            q.append(curr)

            while q:
                u = q.popleft()
                
                # print(color)

                for v in graph[u]:
                    if color[v] == color[u]:
                        return False
                    
                    elif color[v] == -1:
                        color[v] = 1- color[u]
                        q.append(v)
            
            return True


        for i in range(n):
            if color[i] == -1:
                if bfs(i, 0) == False:
                    return False
        
        return True

        
