class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        adj = []
        indegree = [0]*n

        for edge in edges:
            u = edge[0]
            v = edge[1]

            indegree[v] += 1
        
        count = 0
        ans = -1
        for v in range(n):
            if indegree[v] == 0:
                ans = v
                count += 1

        
        if count > 1 :
            return -1
        
        return ans
            

