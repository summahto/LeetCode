class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        
        if groupSize == 1:
            return True

        n = len(hand)
        
        if n % groupSize != 0:
            return False

        c = Counter(hand)
        minHeap = list(c)
        heapq.heapify(minHeap)

        # print(minHeap)

        while minHeap:

            curr_card = minHeap[0]

            for j in range(groupSize):

                if c[curr_card + j] == 0:
                    return False
                
                c[curr_card + j] -= 1

                if c[curr_card + j] == 0:
                    heapq.heappop(minHeap)

        return True

