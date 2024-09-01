class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        
        l = len(original)
        if m*n != l:
            return []

        ans = []
 
        row = []
        for i in range(l):
            row.append(original[i])

            if len(row) == n:
                ans.append(row)
                row = []
            
        # print(ans)

        return ans