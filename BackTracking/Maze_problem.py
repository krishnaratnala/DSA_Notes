'''
it will the total no of paths


def dfs(row, col):
    if row == 1 or col == 1:
        return 1
    down = dfs(row - 1, col)
    right1 = dfs(row, col - 1)
    return down+right1
print(dfs(3,3))

'''

'''
it will print the paths of maze travels
def dfs(p,row, col):
    if row == 1 or col == 1:
        print(p)
        return
    down = dfs(p+'down',row - 1, col)
    right1 = dfs(p+'right',row, col - 1)

print(dfs("",3,3))
'''

def maze_list():
    result=[]
    def dfs(p, row, col):
        if row == 1 and col == 1:
            result.append(p)
            return
        if row>1:
            dfs(p + " " + "down", row - 1, col)
        if col>1:
            dfs(p + " " + "right", row, col - 1)
        if row>1 and col>1:
            dfs(p+"diagonal",row-1,col-1)
    dfs("", 3, 3)
    print(len(result))
    return  result

print(maze_list())
'''
the above code is print the no of paths in  the format of list
include diagonal 
'''