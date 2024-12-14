class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        
        n = len(nums)
        i, j = 0, 0

        # currMin = float('inf')
        # currMax = float('-inf')
        count = 0

        # track the elements in the current window and their frequency
        currWindow = Counter()

        # keep adding jth element into the heap
        minHeap = []
        maxHeap = []

        while j < n:

            heapq.heappush(minHeap, nums[j])    
            heapq.heappush(maxHeap, -1 * nums[j])
            currWindow[nums[j]] += 1

            # as the condition breaks
            while abs((-1 * maxHeap[0]) - minHeap[0]) > 2:
                # slide the window from left: i moves forward
                currWindow[nums[i]] -= 1
                
                if currWindow[nums[i]] == 0:
                    del currWindow[nums[i]]

                # check if the curr top is present in currWindow
                # if not, remove it
                while (-1* maxHeap[0]) not in currWindow:
                    heapq.heappop(maxHeap)
                
                while minHeap[0] not in currWindow:
                    heapq.heappop(minHeap)
                
                i+=1
            
            count += j-i+1
            # print(f"{count=} {j=} {i=}")

            j+= 1
        
        return count