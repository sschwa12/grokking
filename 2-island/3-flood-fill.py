def floodFill(matrix, x, y, newColor):
    old_color = matrix[x][y]
    rows, cols = len(matrix), len(matrix[0])

    def dfs(x, y):
        if x not in range(rows) or y not in range(cols):
            return
        source = matrix[x][y]
        if source != old_color:
            return
        matrix[x][y] = newColor
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        for dr, dc in directions:
            r, c = x + dr, y + dc
            dfs(r, c)
    dfs(x, y)
    return matrix


test_data = [
    [0, 1, 1, 1, 0],
    [0, 0, 0, 1, 1],
    [0, 1, 1, 1, 0],
    [0, 1, 1, 0, 0],
    [0, 0, 0, 0, 0],
]
test_data_example = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 1, 1, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0],
]
test_data_example_last = [
    [1, 2, 1],
    [0, 1, 0],
    [1, 2, 1],
]
print(floodFill(test_data, 1, 3, 2))
print(floodFill(test_data_example, 3, 2, 5))
print(floodFill(test_data_example_last, 0, 1, 3))
