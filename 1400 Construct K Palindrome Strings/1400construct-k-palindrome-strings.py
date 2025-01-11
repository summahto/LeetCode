class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        
        n = len(s)
        freq = Counter(s)

        numPairs = 0
        
        for ch in freq:
            numPairs += freq[ch]//2
        
        
        if k > n:
            return False
        if k == n:
            return True
        
        # print(f"{numPairs=}")

        if (n-k+1)//2 <= numPairs:
            return True

    
        return False