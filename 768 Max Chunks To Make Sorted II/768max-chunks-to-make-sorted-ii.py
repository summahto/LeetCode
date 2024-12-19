class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        
        n = len(arr)
        minArr = [0]* n
        maxArr = [0] * n

        maxSoFar = arr[0]
        minSoFar = arr[-1]

        for i in range(n):
            maxSoFar = max(maxSoFar, arr[i])
            maxArr[i] = maxSoFar

        for i in range(n-1, -1, -1):
            minSoFar = min(minSoFar, arr[i])
            minArr[i] = minSoFar

        chunks = 1        
        for i in range(1, n):
            if maxArr[i-1] <= minArr[i]:
                chunks += 1

        return chunks