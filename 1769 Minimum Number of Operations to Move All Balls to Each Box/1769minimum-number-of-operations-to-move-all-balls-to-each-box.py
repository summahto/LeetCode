class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        
        n = len(boxes)

        leftMoves = [0] *n
        rightMoves = [0] *n
        currMove = 0
        cumMoves = 0
        for i, c in enumerate(boxes):
            currMove += int(c)
            cumMoves += currMove
            leftMoves[i] = cumMoves

        currMove = 0
        cumMoves = 0
        for i in range(n-1, -1, -1):
            currMove += int(boxes[i])
            cumMoves += currMove
            rightMoves[i] = cumMoves

        ans = [0] * n

        # print(leftMoves)
        # print(rightMoves)

        for i in range(n):
            if i - 1 >= 0:
                ans[i] += leftMoves[i-1]

            if  i+1 < n:
                ans[i] += rightMoves[i+1]

        return ans
        