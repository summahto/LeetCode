class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        
        if len(connections) < n-1:
            return -1

        parent = [i for i in range(n)]
        rank = [0] * n

        def find(i, parent):
            if i == parent[i]: 
                return i
            
            parent[i] = find(parent[i], parent)
            return parent[i]

        def union(x, y, parent, rank):
            x_parent = find(x, parent)
            y_parent = find(y, parent)

            if x_parent == y_parent:
                return 
            
            if rank[x_parent] > rank[y_parent]:
                parent[y_parent] = x_parent
            
            elif rank[x_parent] < rank[y_parent]:
                parent[x_parent] = y_parent
            else :

                parent[y_parent] = x_parent
                rank[x_parent] += 1
        

        processed = set()
        extra = 0
        comp = n
        for (u, v) in connections:
            u_parent = find(u, parent)
            v_parent = find(v, parent)

            # processed.add(u)
            # processed.add(v)

            if u_parent == v_parent:
                extra += 1
            else:
                union(u, v, parent, rank)
                comp -= 1
        
        # totalNodesNow = n - len(processed) + 1

        # edgesNeeded = totalNodesNow - 1
        # print(totalNodesNow, extra)

        return comp -1

            
