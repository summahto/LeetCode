class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        
        n = len(grid[0])

        row1Rem = sum(grid[0])
        row2Rem = 0

        # minimize the robot2Points
        robot2Points = float("inf")
        # simiulate for each turnIdx the 1st robot is turning down to the 1st row
        for turnIdx in range(n):
            
            row1Rem -= grid[0][turnIdx]
            # Robot2 wants to maximize the sum it can get in both the paths available to him
            robot2Maximizing = max(row2Rem, row1Rem)
            # Robot1 wants to manimize  the overall num of points R1 can get
            robot2Points = min(robot2Points, robot2Maximizing)

            row2Rem += grid[1][turnIdx]
        
        return robot2Points