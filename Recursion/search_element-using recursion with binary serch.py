def search_target(arr,target):
    s=0
    e=len(arr)
    mid=s-(s-e)//2
    if arr[mid]==target:
        return mid
    if target>arr[mid]:

        return search_target(arr,target)
arr=[1,2,3,4]
target=1
search_target(arr,target)