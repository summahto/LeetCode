class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        superlist = []
        self.backtrack(candidates, target, [], superlist, 0)

        return superlist


    def backtrack(self, candidates, target, curr, superlist, index):

        if(target < 0) :
            return

        if(target == 0) :
            superlist.append(list(curr))
            return

        
        for i in range(index, len(candidates)):
            curr.append(candidates[i])
            self.backtrack(candidates, target - candidates[i], curr, superlist, i)
            curr.pop(-1)

