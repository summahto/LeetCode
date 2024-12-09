from sortedcontainers import SortedSet
from collections import deque

def function(operations):
    obstacles = SortedSet()
    ans = []

    for op in operations:
        if op[0] == 1:
            # Add obstacle
            obstacles.add(op[1])
        else:
            # Check if block can be built
            x, size = op[1], op[2]
            start = x - size

            # Find the first obstacle >= start
            ceiling = obstacles.bisect_left(start)

            # If there's no obstacle in [start, x), we can build
            can_build = ceiling == len(obstacles) or obstacles[ceiling] >= x

            ans.append('1' if can_build else '0')

    return ''.join(ans)


def water_flow_time(heights):
    if not heights or not heights[0]:
        return []

    m, n = len(heights), len(heights[0])
    result = [[-1] * n for _ in range(m)]
    queue = deque()

    # Find the minimum height and add all cells with this height to the queue
    min_height = min(min(row) for row in heights)
    for i in range(m):
        for j in range(n):
            if heights[i][j] == min_height:
                queue.append((i, j, 0))
                result[i][j] = 0

    # Directions: up, down, left, right
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while queue:
        x, y, time = queue.popleft()

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if 0 <= nx < m and 0 <= ny < n and result[nx][ny] == -1:
                if heights[nx][ny] >= heights[x][y]:
                    result[nx][ny] = time + 1
                    queue.append((nx, ny, time + 1))

    return result




if __name__ == '__main__':
    operations= [[1, 2], [1, 5], [2, 5, 2], [2, 6, 3], [2, 2, 1], [2, 3, 2]]

    print(function(operations), )

    heights = [[3, 2, 1], [6, 5, 4], [9, 8, 7]]

    [[-1, 2, 2], [-1, 0, 1], [-1, -1, -1]]

    ans = []
    print(water_flow_time(heights))




# Constraints ???


