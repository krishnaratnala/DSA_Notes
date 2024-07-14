def maze(arr):
    row = len(arr) - 1
    col = len(arr[0]) - 1
    steps1 = []

    def dfs(p,row1, col1, path, step):
        if row1 == row and col1 == col:
            path[row1][col1] = step
            for c in path:
                print(c)
            print(p)
            print()

            return


        arr[row1][col1] = False
        path[row1][col1] = step

        # Move down
        if row1 < row and arr[row1 + 1][col1]:
            dfs(p+"D", row1 + 1, col1, path, step + 1)

        # Move right
        if col1 < col and arr[row1][col1 + 1]:
            dfs(p+"R",row1, col1 + 1, path, step + 1)

        # Move up
        if row1 > 0 and arr[row1 - 1][col1]:
            dfs(p+"U",row1 - 1, col1, path, step + 1)

        # Move left
        if col1 > 0 and arr[row1][col1 - 1]:
            dfs(p+"L",row1, col1 - 1, path, step + 1)

        arr[row1][col1] = True
        path[row1][col1] = 0

    path = [[0 for _ in range(col + 1)] for _ in range(row + 1)]
    dfs("",0, 0, path, 1)
    return steps1


arr = [
    [True, True, True],
    [True, True, True],
    [True, True, True],
    [True, True, True]
]
maze(arr)