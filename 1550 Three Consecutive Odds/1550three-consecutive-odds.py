class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        n = len(arr)

        if n == 1 or n == 2:
            return False
            
        count = 0
        for i in range(2,n):
            if arr[i-2] % 2 !=0 and arr[i-1] % 2 !=0 and arr[i] % 2 !=0:
                return True

        return False