
def combination(arr):
    outerlist = [[]]
    for num in arr:
        n = len(outerlist)
        for i in range(n):
            new_combination = outerlist[i] + [num]
            outerlist.append(new_combination)
    if outerlist[0]==[]:
        outerlist.pop(0)
        return outerlist
arr = [1, 2, 3]
print(combination(arr))