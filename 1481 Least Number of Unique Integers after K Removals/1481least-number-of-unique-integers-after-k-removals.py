class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        
        
        c = Counter(arr)
        vals = list(c.values())
        vals.sort()

        for i,v in enumerate(vals):

            k -= v
            if k < 0:
                return len(vals) - i

        return 0
        