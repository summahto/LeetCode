class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:

        
        grid = [[0] * n for _ in range(m)]

        for w in walls:
            grid[w[0]][w[1]] = 2

        # print(f"{grid=}")
        
        for guard in guards:
            grid [guard[0]][guard[1]] = 3

        def markGuarded(x, y):
            # move up
            for i in range(x+1, m):
                if grid[i][y] in [2, 3]:
                    break
                grid[i][y] = 4

            # move down
            for i in range(x-1, -1, -1):
                if grid[i][y] in [2,3]:
                    break
                grid[i][y] = 4

            # move right
            for j in range(y+1, n):
                if grid[x][j] in [2,3]:
                    break
                grid[x][j] = 4

            # move left
            for j in range(y-1, -1, -1):
                if grid[x][j] in [2,3]:
                    break
                grid[x][j] = 4

        for guard in guards:
            markGuarded(guard[0], guard[1])

        print(f"{grid=}")
        
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    count+=1
        
        return count

        