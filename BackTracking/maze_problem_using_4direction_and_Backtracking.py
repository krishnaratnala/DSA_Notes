def maze(arr):
    row = len(arr) - 1
    col = len(arr[0]) - 1
    result = []

    def dfs(p, row1, col1):
        if row1 == row and col1 == col:
            result.append(p)
            return
        if not arr[row1][col1]:
            return
        arr[row1][col1] = False
        if row1 < row:
            dfs(p + " down", row1 + 1, col1)
        if col1 < col:
            dfs(p + " right", row1, col1 + 1)
        if row1 > 0:
            dfs(p + " up", row1 - 1, col1)
        if col1 > 0:
            dfs(p + " left", row1, col1 - 1)
        arr[row1][col1] = True

    dfs("", 0, 0)
    return result

arr = [
    [True, True, True],
    [True, True, True],
    [True, True, True]
]

print(maze(arr))
