from collections import deque


def max_area_of_island(matrix):
    island_counts = []
    rows, cols = len(matrix), len(matrix[0])

    def bfs_get_counts(row, col):
        q = deque()
        q.append((row, col))
        matrix[row][col] = 0
        count = 1
        while q:
            cur_row, cur_col = q.popleft()
            directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            for dr, dc in directions:
                r = cur_row + dr
                c = cur_col + dc
                if r in range(rows) and c in range(cols) and matrix[r][c] == 1:
                    count += 1
                    q.append((r, c))
                    matrix[r][c] = 0
        return count

    for row in range(rows):
        for col in range(cols):
            if matrix[row][col] == 1:
                island_counts.append(bfs_get_counts(row, col))
    if island_counts:
        return max(island_counts)
    return 0


test_data = [
    [1, 1, 1, 0, 0],
    [0, 1, 0, 0, 1],
    [0, 0, 1, 1, 0],
    [0, 1, 1, 0, 0],
    [0, 0, 1, 0, 0],
]
print(max_area_of_island(test_data))
