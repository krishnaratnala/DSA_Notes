def search_target(arr,target_element):
    n=len(arr)
    if len(arr)<0:
        return -1
    for i in range(len(arr)):
        if arr[i]==target_element:
            return i
    return -1
arr=[1,3,4,5,2]
target_element=4
print(search_target(arr,target_element))

## here iam returing the index value
## here if the element is not found we are returing -1 ,-1 might be one of the element that why we can return "Element is not found"
