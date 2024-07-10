def combination(arr):
    arr.sort()
    outer=[[]]
    for i in range(len(arr)):
        start=0
        n=len(outer)
        end=0
        if (i>0 and arr[i]==arr[i-1]):
            start=end+1
        end=len(outer)-1
        for j in range(start,n):
            combi=outer[j]+[arr[i]]
            outer.append(combi)
    if outer[0]==[]:
        outer.pop(0)
        return outer
arr=[2,1,2]
print(combination(arr))