class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort(key = lambda interval: interval[0])

        ans = []
        ans.append(intervals[0])

        for start,end in intervals[1:]:

            if start <= ans[-1][1]:
                ans[-1][1] = max(ans[-1][1], end)
            
            else :
                ans.append([start, end])
        
        return ans




        # i = 1
        # isNew = True 
        # start = 0
        # while i < len(intervals):
            
        #     if isNew:
        #         part = []
        #         start = intervals[i-1][0]
        #         part.append(start)
            
        #     if intervals[i][0] <= intervals[i-1][1]:
        #         i+= 1
        #         isNew = False
        #         continue
            
        #     isNew = True
        #     part.append(intervals[i-1][1])
        #     ans.append(part)
        
            # print(f"{ans=}")

            
            

        return None