def printing_triangle(n):
    def dfs(r,c):
        if r==0:
            return
        if r>c:
            print('*',end='')
            dfs(r,c+1)
        else:
            print()
            dfs(r-1,0)
    dfs(n,0)
n=4
printing_triangle(n)
'''
def printing_triangle(n):
    def dfs(r,c):
        if r==0:
            return
        if r>c:
            dfs(r,c+1)
            print('*', end='')
        else:
            dfs(r-1,0)
            print()
    dfs(n,0)
n=4
printing_triangle(n)'''