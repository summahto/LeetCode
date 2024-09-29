class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # [a, b] -> must take b first
        # b --- > a
        # adj List = map()
        if not prerequisites:
            return True

        adj = {}

        for i in range(numCourses):
            adj[i] = []

        for pair in prerequisites:
            pre = pair[1]
            crs = pair[0]

            adj[pre].append(crs)

        visited = [False] * numCourses
        inRec = [False] * numCourses

        def cycleDFS(u):
            visited[u] = True
            inRec[u] = True

            for v in adj[u]:
                if not visited[v]:
                    if cycleDFS(v):
                        return True
                
                elif inRec[v]:
                    return True
            
            inRec[u] = False
            return False



        for i in range(numCourses):
            if not visited[i]:
                if cycleDFS(i):
                    return False

        return True

            