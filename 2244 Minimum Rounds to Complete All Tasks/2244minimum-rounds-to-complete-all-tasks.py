class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        
        freq= Counter(tasks)
        rounds = 0
        for k,c in freq.items():
            if c == 1:
                return -1
            
            if c %3 ==0:
                rounds += (c//3)
            else:
                rounds += (c//3) + 1

        return rounds
