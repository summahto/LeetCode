class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        
        pq = []

        for i, num in enumerate(nums):
            heapq.heappush(pq, (num, i))
        
        while k > 0:
            (n, idx) = heapq.heappop(pq)

            nums[idx] *= multiplier

            heapq.heappush(pq, (nums[idx], idx))
            k -=1
        
        return nums

