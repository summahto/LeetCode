class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        
        # node (i, j)
        # edge = 0 if the next node (i+1, j) = 0
        # otherwise edge = 1
        m = len(grid)
        n = len(grid[0])

        adj = {}
        # I already have a graph in the matrix
        # SSP from (0,0) -> (m-1, n-1)
        # shortest ?? least number of obstacles.
        # BFS, can we apply? No, we have edge weights 0 or 1
        # Dijkstra is the right approach
        # what do we need for dijkstra ?
        # PQ, Distance, adj (which is the grid for us), source

        source = (0,0)
        obs = [[float('inf') for _ in range(n)] for a in range(m)]
        obs[0][0] = 0

        # heap of (num of obstacles, (i, j))
        pq = []
        heapq.heappush(pq, (0, 0, 0))
        dirs = [[0,1], [1,0], [-1, 0], [0, -1]]

        while pq:
            (currObs, i, j) = heapq.heappop(pq)
            # already have i, j, go all four directions from here

            if i == m-1 and j == n-1:
                return obs[i][j]

            for di, dj in dirs:
                x = i + di
                y = j + dj

                if x >= m or x < 0 or y < 0 or y >= n:
                    continue
                # print(f"{i=} {j=} {x=} {y=}")

                vObs = currObs + grid[x][y]

                if vObs < obs[x][y]:
                    obs[x][y] = vObs
                    heapq.heappush(pq, (vObs, x, y))

        return obs[m-1][n-1]

                    
