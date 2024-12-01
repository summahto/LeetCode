class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        n = len(arr)

        seen = set()

        for num in arr:
            if num in seen:
                return True
            else :
                if num % 2 == 0:
                    seen.add(num//2)
                
                seen.add(num *2)
        
        return False