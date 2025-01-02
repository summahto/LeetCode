class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        # n = len(s)
        # q= deque(s)

        if len(s) == 1:
            return s

        for d, a in shift:
            a = a % len(s)
            if d == 0:
                s += s[0:a]
                s = s[a:len(s)]
            else:
                s = s[len(s)-a:] + s
                s = s[:len(s)-a]
            
            # print(s)

        return s

