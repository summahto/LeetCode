class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        
        # check : adding a student to which class gives maximum output to the pass ratio
        # keep a max heap of change in pass ratio, along with their current class ratios
        maxHeap = []

        n = len(classes)

        for (numPass, numClass) in classes:
            # calculate the contribution of addition of each
            before = (numPass/numClass)
            after = (numPass + 1)/ (numClass + 1)
            change = after - (numPass/numClass)

            heapq.heappush(maxHeap, (-1* change, numPass, numClass))
        
        # print(f"{maxHeap=}")

        
        for _ in range(extraStudents):
            (bestChange, prevPass, prevClass) = heapq.heappop(maxHeap)

            currPass = prevPass +1
            currClass = prevClass +1 

            nextChange = ((currPass + 1)/(currClass +1) - (currPass/currClass))

            heapq.heappush(maxHeap, (-1* nextChange, currPass, currClass))
            
            extraStudents -= 1

        
        # print(f"{maxHeap=}")

        totalPass = 0.0

        while maxHeap:
            (bestChange, prevPass, prevClass)= heapq.heappop(maxHeap)
            
            totalPass += (prevPass/prevClass)

        # print(f"{totalPass=}")

        return float(totalPass/n)
            

 
