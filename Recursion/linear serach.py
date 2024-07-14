'''
def linear_search(arr,target,s):
    if arr[s]==target:
        return arr[s]
    if s!=target:
        return linear_search(arr,target,s+1)
arr=[1,2,4,18,9]
target=18
s=0
print(linear_search(arr,target,s))
'''

'''
returning the index in the list
'''
def linear_search(arr,target,s):
    if s==len(arr):
        return []
    if arr[s]==target:
         return  [s]+linear_search(arr,target,s+1)
    else:
        return linear_search(arr,target,s+1)
arr=[1,2,3,4,4,5,6,7]
target=4
s=0
print(linear_search(arr,target,s))