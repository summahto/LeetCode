class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        

        pq = []
        total = 0
        for gift in gifts:
            heapq.heappush(pq, -1 * gift)
            total += gift
        
        while k > 0:

            top = heapq.heappop(pq)
            top *= -1
            rem = floor(top** 0.5)

            total -= (top - rem)
            heapq.heappush(pq, -1* rem)

            k-= 1
        
        # print(f"{pq=}")

        return total