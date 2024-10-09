class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        freq = Counter(barcodes)
        # print(freq)
        pq = []

        for code in freq :
            heapq.heappush(pq, (-1 * freq[code] , code))

        # heapq.heapify(pq)

        # print(pq)
        ans = []

        while len(pq) >=  2:

            (count1, code1) = heapq.heappop(pq)
            (count2, code2) = heapq.heappop(pq)

            # count1 = -1 * count1
            # count1 -= 1

            # count2 = -1 * count2
            # count2 -= 1
            
            ans.extend([code1, code2])

            if -1* count1 -1>= 1:
                heapq.heappush(pq, (count1 + 1, code1))
            if -1 * count2 -1 >= 1:
                heapq.heappush(pq, (count2 + 1, code2))

        if pq:
            (count, code) = heapq.heappop(pq)
            ans.append(code)                

        return ans