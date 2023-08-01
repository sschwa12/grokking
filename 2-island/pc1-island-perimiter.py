def island_perimiter(matrix):
    ROWS, COLS = len(matrix), len(matrix[0])
    seen = set()

    def dfs(r, c):
        if r not in range(ROWS) or c not in range(COLS) or matrix[r][c] == 0:
            return 1
        if (r, c) in seen:
            return 0
        seen.add((r, c))
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        return sum([dfs(dr + r, dc + c) for dr, dc in directions])


    for row in range(ROWS):
        for col in range(COLS):
            if matrix[row][col] == 1 and (row, col) not in seen:
                return dfs(row, col)
    return 0

print(island_perimiter([[1,1,0,0,0],[0,1,0,0,0],[0,1,0,0,0],[0,1,1,0,0],[0,0,0,0,0]]))
print(island_perimiter([[0,1,0,1,0,1,0,1,0],[1,0,1,0,1,0,1,0,1],[0,1,0,1,0,1,0,1,0]]))
