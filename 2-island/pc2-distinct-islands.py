def distinct_islands(matrix):
    island_shapes = []
    ROWS, COLS = len(matrix), len(matrix[0])
    seen = set()

    def dfs(r, c, direction):
        if r not in range(ROWS) or c not in range(COLS):
            return ''
        
        if matrix[r][c] == 0 or (r, c) in seen:
            return ''
        seen.add((r, c))
        traversal = direction
        directions = [[1, 0, 'D'], [-1, 0, 'U'], [0, 1, 'R'], [0, -1, 'L']]
        for dr, dc, dir in directions:
            traversal += dfs(dr + r, dc + c, dir)
        return traversal

    for r in range(ROWS):
        for c in range(COLS):
            if matrix[r][c] == 1 and (r, c) not in seen:
                island_shapes.append(dfs(r, c, 'O'))
    return len(set(island_shapes))


s = distinct_islands(
    [
        [1, 1, 0, 1, 1],
        [1, 1, 0, 1, 1],
        [0, 0, 0, 0, 0],
        [0, 1, 1, 0, 1],
        [0, 1, 1, 0, 1],
    ]
)
print(s)