class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        
        boxTypes.sort(key=lambda x: x[1], reverse=True)

        # print(boxTypes)
        n = len(boxTypes)

        totalSize = 0
        total = 0
        for box in boxTypes:
            
            totalSize += box[0]
            # currBox = box[0]
            # currUnit = box[1]
            if totalSize <= truckSize:
                total += box[0] * box[1]

            # print(totalSize, box[0], box[1])
            if totalSize > truckSize:
                total += (box[0] -(totalSize - truckSize))* box[1]
                break
        

        return total