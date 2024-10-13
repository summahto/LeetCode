class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
    

        ans = []
        pq = []
        if a > 0:
            heapq.heappush(pq, (-1* a, 'a'))
        
        if b > 0:
            heapq.heappush(pq, (-1* b, 'b'))
        
        if c > 0:
            heapq.heappush(pq, (-1* c, 'c'))

        # if count of each element is <=2, then directly add them to the answer and return it
        # if (-1* pq[0][0]) <= 2:
        #     while pq:
        #         (count, char) = heapq.heappop(pq)

        #         for _ in range(-1 * count):
        #             ans.append(char)
            
        #     # print(ans)
        #     return ''.join(ans)
        
        # here you know that the 1st element has the count >= 2, because of the previous if condition
        # but what about other chars in the queue  


        while pq:
            (count, char) = heapq.heappop(pq)
            count = -count

            if len(ans) >= 2 and ans[-1] == char and ans[-2] == char:
                if not pq:
                    break

                # pick the next element in the heap
                (count2, char2) = heapq.heappop(pq)
                count2 = -count2
                
                ans.append(char2)
                count2 -= 1

                if count2 >= 1:
                    heapq.heappush(pq, (-1* count2, char2))
            
            else :
                ans.append(char)
                count -= 1

            if count >= 1:
                heapq.heappush(pq, (-1* count, char))

        return ''.join(ans)
    