from collections import deque


data = [
    [0, 1, 1, 1, 0],
    [0, 0, 0, 1, 1],
    [0, 1, 1, 1, 0],
    [0, 1, 1, 0, 0],
    [0, 0, 0, 0, 0],
]

# in case you need strings, like the leetcode problem
str_data = [str(n) for row in data for n in row]


def count_islands(matrix):
    count = 0
    row_count, col_count = len(matrix), len(matrix[0])

    def bfs(x, y):
        q = deque()
        matrix[x][y] = 0
        q.append((x, y))
        while q:
            # change to '.pop()' for dfs
            row, col = q.popleft()
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

            for dr, dc in directions:
                r, c = row + dr, col + dc
                if (
                    r in range(row_count)
                    and c in range(col_count)
                    and matrix[r][c] == 1
                ):
                    q.append((r, c))
                    matrix[r][c] = 0

    for x in range(row_count):
        for y in range(col_count):
            if matrix[x][y] == 1:
                bfs(x, y)
                count += 1
    return count


print(count_islands(data))
