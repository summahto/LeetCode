class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        

        total = sum(chalk)

        rem = k % total
        i = 0

        while rem >= 0:
            rem -= chalk[i]
            i+= 1

        # print(i)

        return i -1
