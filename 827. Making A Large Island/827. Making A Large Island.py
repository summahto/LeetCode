class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        
        m = len(grid)
        n = len(grid[0])

        dirs = [[1,0], [0,1], [-1,0], [0,-1]]

        def dfs(i, j, uniqueId):
            curr = grid[i][j]
            grid[i][j] = uniqueId

            for dx, dy in dirs:
                x = i + dx    
                y = j + dy

                if x < 0 or y < 0 or x == m or y == n or visited[x][y] or grid[x][y] == 0:
                    continue
                
                visited[x][y] = True
                curr += dfs(x, y, uniqueId)

            return curr

        # use a unique ID to represent all the elements in an island
        uniqueId = 2
        # map this unique ID to the area calculated from DFS
        areaMap = defaultdict(int)
        visited = [[False for _ in range(n)] for a in range(m)]

        for i in range(m):
            for j in range(n):
                if not visited[i][j] and grid[i][j] == 1:
                    visited[i][j] = True
                    area = dfs(i, j, uniqueId)
                    areaMap[uniqueId] = area
                    uniqueId += 1
        
        # print(f"{grid=}")
        # print(f"{areaMap=}")

        maxArea = 0
        numZeros = 0

        seen = set()
        for i in range(m):
            for j in range(n):
                
                if grid[i][j] == 0:
                    area = 1
                    numZeros += 1
                    
                    for dx, dy in dirs:
                        x = i + dx    
                        y = j + dy
                        
                        # uniqueId = grid[x][y]
                        if x < 0 or y < 0 or x == m or y == n or grid[x][y] == 0 or grid[x][y] in seen :
                            continue
                        
                        area += areaMap[grid[x][y]]
                        seen.add(grid[x][y])
                    
                    maxArea = max(maxArea, area)
                    seen.clear()


                        
        if numZeros == 0:
            return m*n
        
        if numZeros == m*n:
            return 1

        return maxArea


        # def dfs(i, j, visited):
        #     curr = grid[i][j]

        #     for dx, dy in dirs:
        #         x = i + dx    
        #         y = j + dy

        #         if x < 0 or y < 0 or x == m or y == n or visited[x][y] or grid[x][y] == 0:
        #             continue
                
        #         visited[x][y] = True
        #         curr += dfs(x, y, visited)

        #     return curr
            

        # maxArea = 0
        # numZeros = 0
        # brute force
        # find each 0, convert it to 1 and get the area connected to that 0, if this beats existing max, update it.
        # for i in range(m):

        #     for j in range(n):

        #         if grid[i][j] == 0:
        #             numZeros += 1
        #             visited = [[False for _ in range(n)] for a in range(m)]
        #             visited[i][j] = True
        #             area = 1
        #             area += dfs(i, j, visited)
        #             maxArea = max(maxArea, area)

        # if numZeros == 0:
        #     return m*n


        # return maxArea
