class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        corresMap = defaultdict(int)
        ans = []


        for i in range(len(nums)):
            if nums[i] not in corresMap:
                corresMap[target - nums[i]] = i
            
            else :
                ans.extend([i, corresMap[nums[i]]])
                break
            
            # print(f"{corresMap=}")


        return ans    