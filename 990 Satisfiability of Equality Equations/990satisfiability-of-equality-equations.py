class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        
        parent = {}
        rank = {}

        for i in range(97, 123):
            # print(chr(i))

            parent[chr(i)] = chr(i)
            rank[chr(i)] =  0
        
        # print(parent)
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
                parent[y_parent]= x_parent
            elif rank[x_parent] < rank[y_parent]:
                parent[x_parent] = y_parent
            else :

                parent[x_parent] = y_parent
                rank[y_parent]+= 1
             


        rem = []
        for s in equations:
            if s[1] is '=':
                # put them together as they are equal
                # u_parent = find(s[0])
                # v_parent = find(s[3])

                union(s[0], s[3], parent, rank)

            else :
                # proces not equal values later on
                rem.append(s)

        for st in rem:
            x_parent = find(st[0], parent)
            y_parent = find(st[3], parent)

            if x_parent == y_parent:
                return False

        return True