def selection_sort(arr):
    n=len(arr)
    def dfs(r,c,max):
        if r==0:
            return
        if r>c:
            if arr[max]<arr[c]:
                dfs(r,c+1,c)
            else:
                dfs(r,c+1,max)
        else:
            arr[max],arr[r-1]= arr[r-1],arr[max]
            return dfs(r-1,0,0)
    dfs(n,0,0)
    return arr
arr=[5,4,3,2,1]
print(selection_sort(arr))
