def bubble_sort(arr):
    def dfs(r,c):
        if r==0 :
            return
        if r>c:
            if arr[c]>arr[c+1]:
                arr[c],arr[c+1]=arr[c+1],arr[c]
                return dfs(r,c+1)
            else:
                return dfs(r,c+1)
        else:
            return dfs(r-1,0)
    dfs(len(arr)-1,0)
    return arr
arr=[5,4,6,3,2,1]
print(bubble_sort(arr))
