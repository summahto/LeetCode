class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        
        items.sort() #mlogm
        ans = []
        n = len(items)
        
        max_beauty = 0
        for i in range(n):
            # set max beauty until now for each item in items
            max_beauty = max(max_beauty, items[i][1])
            items[i][1]= max_beauty

        # print(items)
        
        for q in queries:
            # index = bisect_right(items, q, key= lambda x: x[0])
            lo, hi = 0, n
            while lo < hi:
                mid = (lo + hi) // 2
                
                if items[mid][0] <= q:
                    lo = mid +1
                else:
                    hi = mid

            index = lo

            if index >= 1:
                ans.append(items[index-1][1])
            else:
                ans.append(0)
            


        return ans