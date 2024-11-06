class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        m = len(s)
        n = len(goal)
        
        if m != n:
            return False
        
        concat = s + s

        return goal in concat
