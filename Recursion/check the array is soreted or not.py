def helper(arr, s, e):
    if e==len(arr):
        return True
    if arr[s]<arr[e]:
        return helper(arr,s+1,e+1)
    return False
def sor_arr(arr):
    s=0
    e=1
    if len(arr)==1 and len(arr)==0:
            return arr
    return helper(arr,s,e)
arr=[1,2,3,5,6,7]
print(sor_arr(arr))