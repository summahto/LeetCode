class Solution:
    def maxRemoval(self, nums: List[int], queries: List[List[int]]) -> int:
        
        queries.sort()
        n = len(nums)
        available = []
        chosen = []

        queries_used = 0
        # i -> index of nums
        # j -> keep track of queries
        j = 0
        for i in range(n):

            # push all the queries which are eligible to take 
            # just add them to available, worry about reducing to 0 when moving elements from available ->chosen
            while j < len(queries) and queries[j][0] == i :
                heapq.heappush(available, -1 * queries[j][1]) 
                j+= 1
            
            curr = nums[i]
            # choose the top nums[i] queries out of available and move them to chosen
            while available and i <= (-1 * available[0]) and len(chosen) < curr:
                heapq.heappush(chosen, (-1 * heapq.heappop(available)))
                # nums[i] -= 1 # chosen still has enough ele, then we never enter this and nums[i] does not ->0
                # still using the existing chosen queries
                queries_used += 1
            
            # print(f"{chosen=}")

            # since chosen -> min_heap, if nums[i] < top endpoint, it is less than all endpoints in chosen
            nums[i] -= len(chosen) #can go -ve but that does not matter

            # print(f"{nums[i]=} {i=}")
            # if we do not have enough queries in available to reduce nums[i] -> 0
            if nums[i] > 0:
                return -1
            
            #We have already processed ele at i, so remove all the queries which end at i
            while chosen and i >= chosen[0]:
                heapq.heappop(chosen)
            

        return len(queries) - queries_used
            