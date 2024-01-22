class Solution:
    def findErrorNums(self, nums):
        res = [0,0] # duplicate, missing

        c1 = Counter(nums)

        for i in range(1, len(nums)+1):
            if c1[i] == 2:
                res[0] = i
            
            if c1[i] == 0:
                res[1] = i

        return res


        



