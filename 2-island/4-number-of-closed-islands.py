from collections import deque


def count_closed_islands(matrix):
    count = 0
    row_len, col_len = len(matrix), len(matrix[0])
    seen = set()

    def dfs(row, col):
        if row not in range(row_len) or col not in range(col_len):
            return 0
        if matrix[row][col] == 0 or (row, col) in seen:
            return 1
        seen.add((row, col))
        
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        print([dfs(dr, dc) for dr, dc in directions])
        return min([dfs(dr + row, dc + col) for dr, dc in directions])

    for row in range(row_len):
        for col in range(col_len):
            if matrix[row][col] == 1 and (row, col) not in seen:
                count += dfs(row, col)
    return count


print(
    count_closed_islands(
        [
            [1, 1, 0, 0, 0],
            [0, 1, 0, 0, 0],
            [0, 0, 1, 1, 0],
            [0, 1, 1, 0, 0],
            [0, 0, 0, 0, 0],
        ]
    )
)
