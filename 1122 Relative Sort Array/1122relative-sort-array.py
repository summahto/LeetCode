class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        
        countMap = Counter(arr1)

        res = []
        for num in arr2:
            # uniq.add(num)
            while countMap[num] != 0:
                res.append(num)
                countMap[num] -= 1
            
            del countMap[num]

        rem = []
        for k, v in countMap.items():
            while v!= 0:
                rem.append(k)
                v -= 1
        
        rem.sort()

        # for num in rem:
        #     res.append(num)
        res += rem

        return res    