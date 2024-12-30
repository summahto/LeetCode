class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        
        zeros = '0' * zero
        ones = '1' * one

        m = len(zeros)
        n = len(ones)
        
        # print(f"{zeros=} {ones=}")
        
        def recurse(length, dp) -> int:
            
            if length > high:
                return 0
            
            if dp[length] != -1 :
                return dp[length]

            count = 0
            if length >= low and length <= high:
                # return 1 + recurse(length + m) + recurse(length + n)
                count +=1
            
            count+= recurse(length + zero, dp)
            count+= recurse(length + one, dp)
            
            dp[length] = count % (10**9 + 7)
            
            return dp[length] 
            # return (recurse(length + m) + recurse(length + n)) 
        
        dp = defaultdict(lambda: -1)
        
        return recurse(0, dp)
