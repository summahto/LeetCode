class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        
        n = len(nums)
        ans =[]
        # Multiple options based on whether subarray at ith index is chosen or not

        # this will decide whether we choose the curr sub arr or not
        def recurse(i, count, ans, memo):
            if count == 0:
                return
            
            if i >= len(sums):
                return            

            sumAtITaken = sums[i] + getMaxSum(i+k, count -1, memo)
            sumAtINotTaken = getMaxSum(i+1, count, memo)
 
            if sumAtITaken >= sumAtINotTaken:
                ans.append(i)
                recurse(i+k, count - 1, ans, memo)
            else:
                recurse(i+1, count, ans, memo)
        
        def getMaxSum(i, count, memo) -> int:
            
            if count == 0:
                return 0 # no more sum needs to be calculated
            # count is not 0 but we have reached the end of the array
            # return an invalid value
            if i >= len(sums):
                return float("-inf") if count > 0 else 0

            if memo[i][count] != -1:
                return memo[i][count]
            
            sumTaken = sums[i] + getMaxSum(i+k, count-1, memo) 
            sumNotTaken = getMaxSum(i+1, count, memo)

            memo[i][count] = max(sumTaken, sumNotTaken)
            return memo[i][count]

        # pre calculate the sums at each index of length k
        i = 0
        j = 0
        sums = []
        
        s = 0
        while j<n:
            s += nums[j]

            if j-i+1 ==k:
                sums.append(s)
                s-= nums[i]
                i+=1
                 
            j+= 1
        
        # print(f"{sums=}")
        
        memo = [[-1] * 4 for _ in range(n)]
        ans = []
        recurse(0, 3, ans, memo)
        
        return ans


