class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        
        n = len(nums)
        
        # sums = []
        ans = 0
        min_heap = []

        for i in range(n):
            # push the pair of element and the index at which it is ending into the heap
            heapq.heappush(min_heap, (nums[i], i))

        # print(min_heap)
        # you can run the loop till the right value, instead of getting all the sums
        # while min_heap:
        j = 1
        while j <= right:


            curr_sum , idx = heapq.heappop(min_heap)

            if j >= left:
                # sums.append(curr_sum)
                ans += curr_sum
            
            if idx + 1 < n:
                next_sum = curr_sum + nums[idx+ 1]
                heapq.heappush(min_heap,(next_sum, idx + 1))

            j += 1

        # print(sums)
        
        # ans = 0
        # for i in range(left-1, right):
        #     ans += sums[i]

        return ans %(10** 9 + 7)
        