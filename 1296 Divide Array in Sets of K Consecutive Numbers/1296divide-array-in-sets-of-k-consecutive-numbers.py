class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        
        n = len(nums)

        if n % k != 0:
            return False

        c = Counter(nums)

        minHeap = list(c.keys())
        heapq.heapify(minHeap)

        while minHeap:

            curr_num = minHeap[0]

            for i in range(k):
                if c[curr_num + i] == 0:
                    return False
                
                c[curr_num + i] -= 1

                if c[curr_num + i] == 0:
                    if curr_num + i != heapq.heappop(minHeap) :
                        return False

        return True