class RandomizedSet:

    def __init__(self):
        self.nums = []
        self.numPosMap = {}
        # self.size = 0

    def insert(self, val: int) -> bool:

        if val not in self.numPosMap.keys():
            self.nums.append(val) 
            self.numPosMap[val] = len(self.nums) -1
            return True

        else :
            return False
        
# Mistakes done : 1. doing the opposite to check emptiness
# coming from Java we have functions like q.isEmpty() and to check whether q is not empty what i generally do is :
# if !q.isEmpty() : #do something

# However, Here it is different when you use : if not self.rset -> this means if the set is empty then you are negating it so this logic will be implemented if the set was empty. 

# 2. checking emptiness and then trying to remove an element.
# If the set is not empty that does not mean the 'val' is present in the set, check is the val is present in the set or not.
    def remove(self, val: int) -> bool:

        # print(self.nums, self.numPosMap)
# Instead of removing the element first and then putting the last element into the removeIdx, move the last element to removeIdx and then pop that element from the dict and last element from the array. 
        if val in self.numPosMap:
            removeIdx = self.numPosMap[val]
            lastNum = self.nums[-1]
            # print(removeIdx, removedNum)

            self.nums[removeIdx] = lastNum
            self.numPosMap[lastNum] = removeIdx
            del self.numPosMap[val]
            self.nums.pop()
            
            return True

        else :
            return False
        

    def getRandom(self) -> int:
        return random.choice(self.nums)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()