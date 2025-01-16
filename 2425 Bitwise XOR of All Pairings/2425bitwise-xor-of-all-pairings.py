class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        
        ans = 0
        xor1 = 0
        xor2 = 0

        m = len(nums1)
        n = len(nums2)

        for n1 in nums1:
            xor1 ^= n1
        
        for n2 in nums2:
            xor2 ^= n2
        
        if n %2 == 0:
            xor1 = 0 
        
        if m%2 == 0:
            xor2 = 0

        return xor1 ^ xor2