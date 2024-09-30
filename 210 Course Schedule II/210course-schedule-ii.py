class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        adj = {}

        for i in range(numCourses):
            adj[i] = []

        for (crs, pre) in prerequisites:
            adj[pre].append(crs)
        
        # print(adj)

        visited = [False] * numCourses
        inRec = [False] * numCourses
        stack = []

        def cycle_dfs(u):
            # if visited[u]:
            #     return

            visited[u] = True
            inRec[u] = True

            for v in adj[u]:
                if not visited[v]:
                    if cycle_dfs(v):
                        return True
                
                elif inRec[v] :
                    return True
            
            inRec[u] = False
            stack.append(u)
            return False

        for i in range(numCourses):
            if not visited[i]:
                if cycle_dfs(i):
                    return []
        

        # print(stack, len(stack))

        ans = []

        while stack:
            ans.append(stack.pop())

        return ans