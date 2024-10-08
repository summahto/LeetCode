class Solution:
    def taskSchedulerII(self, tasks: List[int], space: int) -> int:

        taskPosMap = {}
        currPos = 0

        # taskPosMap[tasks[0]] = 0
        # currPos +=1
        
        # for i in range(1, len(tasks)):

        #     if taskPosMap[tasks[i]] != -1:
        #         # task was seen before
        #         prevPos = taskPosMap[tasks[i]]
        #         spacesBetween = currPos - prevPos -1

        #         if spacesBetween >= space:
        #             taskPosMap[tasks[i]] = currPos
        #         else:
        #             spacesNeeded = space - spacesBetween
        #             currPos += spacesNeeded
        #             taskPosMap[tasks[i]] = currPos

        #     else :
        #         taskPosMap[tasks[i]] = currPos

        #     # print(i, taskPosMap)

        #     currPos += 1

        for task in tasks:
            
            if task in taskPosMap:
                prevPos = taskPosMap[task]
                currPos = max(prevPos + space, currPos) + 1
                taskPosMap[task] = currPos
            else:
                currPos += 1
                taskPosMap[task] = currPos

        return currPos 

