class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        
        events.sort()
        pq = []
        max_val = 0
        max_sum = 0

        # print(f"{events=}")

        for (si, ei, vi) in events:
            
            # taken care of it in "vi" of #22
            # max_sum = max(max_sum, vi)

            # print(f"{pq=} {si=} {max_sum=}")

            while pq and si > pq[0][0]:
                (ej, vj) = heapq.heappop(pq)
                max_val = max(max_val, vj)
            
            max_sum = max(max_sum, max_val + vi)
            heapq.heappush(pq, (ei, vi))

        
        return max_sum