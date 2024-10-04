class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        n = len(edges)
        parent = [i for i in range(1, n+1)]
        rank = [0] * n
        
        # print(parent)

        def find(i):
            if i == parent[i-1]:
                return i

            parent[i-1] = find(parent[i-1])
            return parent[i-1]
        
        def union(x, y):
            x_parent = find(x)
            y_parent = find(y)

            if x_parent == y_parent:
                return
            
            if rank[x_parent -1] > rank[y_parent - 1]:
                parent[y_parent- 1] = x_parent

            elif rank[x_parent - 1] < rank[y_parent -1]:
                parent[x_parent- 1] = y_parent

            else :
                parent[y_parent -1] = x_parent
                rank[x_parent -1] +=1
                
        ans = [0]*2
        for (u, v) in edges:
            u_parent = find(u)
            v_parent = find(v)

            if u_parent != v_parent:
                union(u, v)
            else :
                ans[0] = u
                ans[1] = v

        return ans
        
