'''

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    # Find the middle point
    m = len(arr) // 2

    # Recursively sort the two halves
    l = merge_sort(arr[:m])
    r = merge_sort(arr[m:])

    # Merge the sorted halves
    return merge(l, r)

def merge(l, r):
    result = []
    i = j = 0

    # Merge the two lists
    while i < len(l) and j < len(r):
        if l[i] < r[j]:
            result.append(l[i])
            i += 1
        else:
            result.append(r[j])
            j += 1

    # Add remaining elements of left list, if any
    while i < len(l):
        result.append(l[i])
        i += 1

    # Add remaining elements of right list, if any
    while j < len(r):
        result.append(r[j])
        j += 1
    return result
arr = [5, 4, 3, 2, 1]
print(merge_sort(arr))

'''
'''
using inplace because space complexity for above code the space complexity is o(n) 
by using inplace the space complexity is o(1)
'''


def merge(arr, s, m, e):
    start2 = m + 1
    if arr[m] <= arr[start2]:
        return
    while s <= m and start2 <= e:

        if arr[s] <= arr[start2]:
            s += 1
        else:
            value = arr[start2]
            index = start2
            while index != s:
                arr[index] = arr[index - 1]
                index -= 1

            arr[s] = value
            s += 1
            m += 1
            start2 += 1
def merge_sort(arr, s, e):
    if s < e:
        m = s + (e - s) // 2

        merge_sort(arr, s, m)
        merge_sort(arr, m + 1, e)

        merge(arr, s, m, e)


arr = [5, 4, 3, 2, 1]
merge_sort(arr, 0, len(arr) - 1)
print(arr)
