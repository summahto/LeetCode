def find_local_maxima(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    result = []

    def check_local_maximum(i, j, value):
        # Calculate region size based on the element value
        region_size = value * 2 + 1
        half_size = region_size // 2

        # Check the entire region
        for di in range(-half_size, half_size + 1):
            for dj in range(-half_size, half_size + 1):
                new_i, new_j = i + di, j + dj

                # Skip if outside matrix bounds
                if not (0 <= new_i < rows and 0 <= new_j < cols):
                    continue

                # Skip corners of the region
                if abs(di) == half_size and abs(dj) == half_size:
                    continue

                # Skip the center element itself
                if di == 0 and dj == 0:
                    continue

                # If any element in region is >= value, not a local maximum
                if matrix[new_i][new_j] >= value:
                    return False

        return True

    # Check each non-zero element
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] > 0:  # Only check non-zero elements
                if check_local_maximum(i, j, matrix[i][j]):
                    result.append([i, j])

    return result


if __name__ == '__main__':
    # Test with the example
    matrix = [
        [3, 0, 0, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 2, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 3, 0, 0, 3]
    ]

    print(find_local_maxima(matrix))  # Output: [[0, 0], [2, 2]]