class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        angrmMap = {}
        
        for s in strs:
            sortedList = sorted(s)
            sortedStr = ''.join(sortedList)
            
            if sortedStr in angrmMap:
                angrmMap[sortedStr].append(s)
            else :
                angrmMap[sortedStr] = [s]

        
        
        return list(angrmMap.values())