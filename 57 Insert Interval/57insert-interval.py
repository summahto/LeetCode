class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        if not intervals:
            return [newInterval] if newInterval else []

        intervals.append(newInterval)
        intervals.sort(key = lambda x : x[0])

        merged = []

        i = 0
        ns = newInterval[0]
        ne = newInterval[1]

        n = len(intervals)
        # non-overlapping events before new Event
        while i< n:
            si = intervals[i][0]
            ei = intervals[i][1]

            if ei < ns:
                merged.append([si, ei])
            else :
                break

            i+= 1

        # Overlapping events
        mergeStart = ns
        mergeEnd = ne
        while i < n:
            si = intervals[i][0]
            ei = intervals[i][1]

            if (si < ns and ei >= ns) or (si >= ns and ei <= ne) or (si <= ne and ei > ne):
 
                mergeStart= min(mergeStart, si)
                mergeEnd= max(mergeEnd, ei)
            else :
                break

            i += 1
    
        merged.append([mergeStart, mergeEnd])

        # non-overlapping events after new Event
        while i < n:
            si = intervals[i][0]
            ei = intervals[i][1]

            if si > ne:
                merged.append([si, ei])
            
            i+=1

        return merged