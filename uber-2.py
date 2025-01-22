# def count_overlapping_crystal_fields(centers):
#     n = len(centers)
#     overlap_count = 0
#
#     # Compare each crystal with every other crystal
#     for i in range(n):
#         for j in range(i + 1, n):  # Start from i+1 to avoid counting same pair twice
#             # Get coordinates of both crystals
#             x1, y1 = centers[i]
#             x2, y2 = centers[j]
#
#             # Check if fields overlap
#             # Fields overlap if difference in x and y coordinates is at most 2
#             if abs(x1 - x2) <= 2 and abs(y1 - y2) <= 2:
#                 overlap_count += 1
#
#     return overlap_count


from collections import defaultdict


def count_overlapping_crystal_fields_optimized(centers):
    # Create a grid with cell size of 2 units
    # Any crystals that could possibly overlap must be in adjacent grid cells
    grid = defaultdict(list)

    # Place each crystal in its corresponding grid cell
    for i, (x, y) in enumerate(centers):
        # Integer division by 2 to determine grid cell
        cell_x, cell_y = x // 2, y // 2
        grid[(cell_x, cell_y)].append((x, y, i))

    overlap_count = 0

    # For each crystal, only check crystals in adjacent cells
    for cell_x, cell_y in grid:
        # Get list of cells to check (current cell and adjacent cells)
        cells_to_check = [
            (cell_x + dx, cell_y + dy)
            for dx in [-1, 0, 1]
            for dy in [-1, 0, 1]
        ]

        # Check crystals in current cell with each other
        crystals = grid[(cell_x, cell_y)]
        for i in range(len(crystals)):
            x1, y1, idx1 = crystals[i]

            # Check against other crystals in same cell
            for j in range(i + 1, len(crystals)):
                x2, y2, idx2 = crystals[j]
                if abs(x1 - x2) <= 2 and abs(y1 - y2) <= 2:
                    overlap_count += 1

            # Check against crystals in adjacent cells
            for adj_x, adj_y in cells_to_check:
                if (adj_x, adj_y) <= (cell_x, cell_y):
                    continue  # Avoid counting pairs twice

                for x2, y2, idx2 in grid[(adj_x, adj_y)]:
                    if abs(x1 - x2) <= 2 and abs(y1 - y2) <= 2:
                        overlap_count += 1

    return overlap_count

if __name__ == '__main__':

    # Test
    centers = [[1, 1], [2, 2], [0, 4]]
    print(count_overlapping_crystal_fields_optimized(centers))  # Output: 2


# # Test with the example
# centers = [[1, 1], [2, 2], [0, 4]]
# print(count_overlapping_crystal_fields(centers))  # Output: 2