class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        outer = []
        candidates.sort()

        self.backtrack(candidates, outer, [], 0, target)
        return outer
        

    def backtrack(self, cand, outer, inner, start, target):

        if(target < 0):
            return

        elif(target == 0) :
            outer.append(list(inner))
            return
        
        else :
            for i in range(start, len(cand)):
                if( start < i and cand[i] == cand[i-1]):
                    continue

                inner.append(cand[i])
                self.backtrack(cand, outer, inner, i+1, target - cand[i])
                inner.pop(-1)