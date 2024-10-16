class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        m = len(grid)
        n = len(grid[0])

        visited = []
        for i in range(m):
            visited.append([0]* n)

        # print(visited)

        dirs = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        
        def dfs(i, j):

            if i < 0 or i >= m or j<0 or j >= n or visited[i][j] or grid[i][j] != "1":
                return

            # print(f"{i=} {j=}")
            visited[i][j] = 1

            dfs(i+1, j)
            dfs(i-1, j)
            dfs(i, j+1)
            dfs(i, j-1)

            

        islands = 0
        for i in range(m):
            for j in range(n):

                if not visited[i][j] and grid[i][j] == "1":
                    dfs(i, j)
                    islands += 1
        
        # print(f"{visited=}")
        
        return islands
