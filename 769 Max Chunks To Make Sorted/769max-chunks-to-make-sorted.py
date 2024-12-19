class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        # [1, 0, 2, 3, 4]
        # find the first pivot point
        n = len(arr)
        # 1
        # Main idea : when can you create a chunk.
        # Only when the max(arr[:i+1]) < min(arr[i+1:]) 
        # That is max of prefix array is less than min of suffix array at i

        # 2 
        # sum of the numbers until now should be the same
        # wherever it is same you can create a partition

        prefixSum = 0
        chunks = 0
        arrSum = 0
        for i in range(n):
            prefixSum += i
            arrSum += arr[i]

            if arrSum == prefixSum:
                chunks += 1

        return chunks

        
        