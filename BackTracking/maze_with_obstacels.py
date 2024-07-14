def maze():
    result = []
    def dfs(p, row, col):
        if row == 1 and col == 1:
            result.append(p)
            return
        if row > 1 and not (row == 2 and col == 2):
            dfs(p + " down", row - 1, col)
        if col > 1 and not (row == 2 and col == 2):
            dfs(p + " right", row, col - 1)

    dfs("", 3, 3)
    return result


print(maze())
