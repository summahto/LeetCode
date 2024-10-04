class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        parent = [i for i in range(n)]
        rank = [0] * n

        def find(i):

            if i == parent[i]:
                return i
            
            parent[i] = find(parent[i])
            return parent[i]

        def union(x_parent, y_parent):
            # x_parent = find(x)
            # y_parent = find(y)

            # if x_parent == y_parent:
            #     return
            
            if rank[x_parent] > rank[y_parent]:
                parent[y_parent] = x_parent
                # componentsCount[x_parent] += 1
            
            elif rank[x_parent] < rank[y_parent]:
                parent[x_parent] = y_parent
                # componentsCount[y_parent] += 1
            
            else : 
                parent[y_parent] = x_parent
                rank[x_parent] += 1
                # componentsCount[x_parent] += 1
            # print("p=", parent)
        
        # componentsCount = defaultdict(lambda:1)
        numComps = n
        for (u, v) in edges:
            u_parent = find(u)
            v_parent = find(v)
            if  u_parent != v_parent:
                union(u_parent, v_parent)
                numComps -= 1
        
        # if numComps < 2:
        #     return 0

        cntMap = defaultdict(int)

        for i in range(n):
            p = find(i)
            cntMap[p] += 1
        
        # print(parent)
        # print(cntMap)
        
        sum = 0

        for (parent,count) in cntMap.items():
            sum +=  count* (n - count)
            n = n-count


        return sum
            