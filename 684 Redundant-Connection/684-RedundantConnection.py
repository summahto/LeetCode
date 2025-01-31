class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # thinking it thorugh
        # parse through each edge one by one
        # 

        adj = defaultdict(list)

        def dfs(u, target, visited):
            visited[u] = True

            if u == target:
                return True

            for v in adj[u]:
                if visited[v]:
                    continue
                
                if dfs(v, target, visited):
                    return True
            
            return False
                
        # missed this
        # clearly mentioned in the question that there are n edges
        # the extra edge converts the tree into a graph
        # not sure why I was getting the max number from the vertices.


        n = len(edges)
        for u, v in edges:

            visited = [False] * (n+1)
            if u in adj and v in adj and dfs(u, v, visited):
                return [u, v]
            else:
                adj[u].append(v)
                adj[v].append(u)
            
        return []

        
        
