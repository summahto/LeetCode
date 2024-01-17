class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        
        c = Counter(arr)
        uniq = set()

        for val in c.values():
            
            if val in uniq:
                return False
            
            else :
                uniq.add(val)

        return True