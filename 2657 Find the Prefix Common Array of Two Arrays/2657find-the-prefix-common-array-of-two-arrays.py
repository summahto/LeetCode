class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        
        n = len(A)
        # c = Counter()
        c = [0] *51
        curr = 0

        ans = []
        for i in range(n):

            c[A[i]] += 1
            c[B[i]] += 1

            if A[i] == B[i] and c[A[i]] == 2:
                curr += 1
            else:
                if c[A[i]] == 2:
                    curr += 1

                if c[B[i]] == 2:
                    curr += 1

            
            ans.append(curr)
                    
        return ans