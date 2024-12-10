class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        # queries.sort(key =lambda x: x[0])
        n = len(queries)
        ans = [False] * n
        viol = []

        for i in range(1, len(nums)):
            if (nums[i] & 1) == (nums[i-1] & 1):
                viol.append(i)

        # print(f"{viol=}")

        def binarySearch(queries, start, end):

            lo, hi = 0, len(viol) -1
            
            # if lo == hi == 0:
            #     return viol[0] >= start and viol[0] <= end

            while lo <= hi:
                mid = (lo + hi)//2

                viol_idx = viol[mid]

                if viol_idx < start:
                    lo = mid +1
                elif viol_idx > end:
                    hi = mid -1
                else :
                    return True
                    
            return False


        for i in range(len(queries)):

            start = queries[i][0] + 1
            end = queries[i][1]

            found_viol_idx = binarySearch(queries, start, end)
            # print(f"{start=} {end=}")
            
            if found_viol_idx:
                ans[i] = False
            else:
                ans[i] = True
  
        return ans