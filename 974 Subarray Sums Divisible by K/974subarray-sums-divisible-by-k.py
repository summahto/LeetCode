class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        
        c = defaultdict(int)
        c[0] = 1
        sum, ans = 0, 0
    
        for num in nums:
            sum += num

            rem = sum % k 
            ans += c[rem]
            c[rem] += 1

        return ans

                
            
        