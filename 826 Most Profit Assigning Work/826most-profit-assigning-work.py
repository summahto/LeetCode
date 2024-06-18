class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        n = len(profit)
        diff_profit= []

        # for i in range(n):
        #     diff_profit.append((difficulty[i], profit[i]))

        # diff_profit.sort()

        diff_profit = sorted(zip(difficulty, profit))
        worker.sort()

        # maxHeap = []
        maxProfit = 0
        # print(diff_profit)
        j = 0
        best = 0
        for diffWorker in worker:
            
            while j< n and diffWorker >= diff_profit[j][0]:
                
                # heapq.heappush(maxHeap, (diff_profit[j][1] * -1))
                best = max(best, diff_profit[j][1])
                j +=1
            
            # if maxHeap:
            #     maxProfit += (maxHeap[0] * -1)
            maxProfit += best

        return maxProfit