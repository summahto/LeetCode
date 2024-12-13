class Solution:
    def findScore(self, nums: List[int]) -> int:
        
        # store (element, index) in heap -> index will help mark marked. elements 
        pq = []
        marked = set()
        score = 0
        n = len(nums)

        for i in range(n):
            heapq.heappush(pq, (nums[i], i))
        

        while pq:

            (ele, idx) = heapq.heappop(pq)

            if idx not in marked:
                score += ele

                # if element is not marked only then check its adj elements and put them in set
                if idx - 1 >= 0:
                    marked.add(idx -1)
                
                if idx + 1 < n:
                    marked.add(idx +1)

        return score
            
            