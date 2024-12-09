def max_sum_submatrix(matrix, size):
    rows = len(matrix)
    cols = len(matrix[0])
    dp = [[0] * cols for _ in range(rows)]
    print(dp)

    for i in range(rows):
        for j in range(cols):
            dp[i][j] = matrix[i][j]
            if i > 0:
                dp[i][j] += dp[i - 1][j]
            if j > 0:
                dp[i][j] += dp[i][j - 1]
            if i > 0 and j > 0:
                dp[i][j] -= dp[i - 1][j - 1]
    max_sum = float('-inf')
    for i in range(size - 1, rows):
        for j in range(size - 1, cols):
            submatrix_sum = dp[i][j]
            if i >= size:
                submatrix_sum -= dp[i - size][j]
            if j >= size:
                submatrix_sum -= dp[i][j - size]
            if i >= size and j >= size:
                submatrix_sum += dp[i - size][j - size]
            if submatrix_sum > max_sum:
                max_sum = submatrix_sum
                max_submatrix = [row[j - size + 1:j + 1] for row in matrix[i - size + 1:i + 1]]
    return max_submatrix


matrix = [[9, 7, 8, 9, 2],
          [6, 9, 9, 6, 1],
          [4, 10, 1, 3, 10],
          [18, 2, 3, 9, 3],
          [4, 6, 8, 5, 21]]
size = 3
max_submatrix = max_sum_submatrix(matrix, size)
print("Maximum sum {} x {} matrix is".format(size, size))
for row in max_submatrix:
    print(" ".join(str(x) for x in row))
