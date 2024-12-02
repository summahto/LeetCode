class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:

        if grid[0][1] > 1 and grid[1][0] > 1:
            return -1

        m = len(grid)
        n = len(grid[0])

        t = 0
        # use dijkstra with time `t` as the distance
        pq = []
        times = [[float('inf') for _ in range(n)] for _ in range(m) ]
        # pq -> t , row, col
        # visited : to keep track of visited cells
        visited = set()
        pq = [(0, 0, 0)]
        dirs = [[0,1], [1, 0], [0, -1], [-1, 0]]

        # if nearby cells > the curr cell, oscillate between any neigbour
        # 0 -- 1 -- 4 : 0-> 1 (t =1) , but cannot proceed further, lets assume all the neighbours are greater
        # 1 -> 0 (t=2), 0 -> 1(t=3), 1 -> 4 (t=4), so now we can proceed

        while pq:

            currTime, i, j = heapq.heappop(pq)

            if i == m-1 and j == n-1:
                return currTime
            
            # adding only once
            # if (i, j) in visited :
            #     continue
            
            
            for di, dj in dirs:
                x = i+ di
                y = j+ dj

                if x < 0 or x >= m or y < 0 or y>= n or (x, y) in visited:
                    continue
                # adding 4 of the neighbours in visted at once
                visited.add((x, y))

                if currTime >= grid[x][y]:
                    heapq.heappush(pq, (currTime + 1, x, y))

                else:
                    diff = grid[x][y] - currTime

                    if  diff % 2 != 0:
                        heapq.heappush(pq, (currTime + diff, x, y))
                    else :
                        heapq.heappush(pq, (currTime + diff + 1, x, y))

                
        return -1



        

        
        
