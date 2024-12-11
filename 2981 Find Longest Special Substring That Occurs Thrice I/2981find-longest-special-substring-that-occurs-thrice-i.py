class Solution:
    def maximumLength(self, s: str) -> int:
        
        # i, j = 0,1
        n = len(s)
        countMap = defaultdict(int)

        for i in range(n):
            countMap[s[i]] += 1 

            for j in range(i+1, n):
                if s[j] != s[i]:
                    break
                countMap[s[i:j+1]]+= 1


        sortedMap = sorted(countMap.items(), key= lambda x: x[1], reverse=True)
        
        # print(f"{countMap=}")
        # print(f"{sortedMap=}")
        
        max_len = -1
        for (key, val) in sortedMap:
            if val >= 3:
                max_len = max(max_len, len(key))
            else :
                break
        
        return max_len