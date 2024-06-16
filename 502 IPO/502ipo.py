from sortedcontainers import SortedList

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:

        n = len(profits)
        total = w
        
        capSortedList = []
        for i in range(n):
            capSortedList.append((capital[i], profits[i]))
        
        capSortedList.sort()
        # print(capSortedList)

        maxHeap = []

        i = 0
        while k > 0:
            
            # print("w : ", w)
            while i < n and capSortedList[i][0] < (w+1):
                # print(profits[i])
                heapq.heappush(maxHeap, capSortedList[i][1]* -1)
                i+=1

            # print(maxHeap)
            if maxHeap :
                cMax = heapq.heappop(maxHeap)
                cMax *= -1
                # print(f"cMax = {cMax}, total = {total}")
                w += cMax
                total+= cMax


            k-=1


        return total



        