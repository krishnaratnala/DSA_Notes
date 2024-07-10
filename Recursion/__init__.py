# Python3 for finding sum of all
# unique subarray sum

# function for finding grandSum
def findSubarraySum(arr, n):
    # calculate cumulative sum of array
    # cArray[0] will store sum of zero elements
    cArray = [0 for i in range(n + 1)]
    for i in range(0, n, 1):
        cArray[i + 1] = cArray[i] + arr[i]

    subArrSum = []

    # store all subarray sum in vector
    for i in range(1, n + 1, 1):
        for j in range(i, n + 1, 1):
            subArrSum.append(cArray[j] -
                             cArray[i - 1])

    # sort the vector
    subArrSum.sort(reverse=False)

    # mark all duplicate sub-array
    # sum to zero
    totalSum = 0
    for i in range(0, len(subArrSum) - 1, 1):
        if (subArrSum[i] == subArrSum[i + 1]):
            j = i + 1
            while (subArrSum[j] == subArrSum[i] and
                   j < len(subArrSum)):
                subArrSum[j] = 0
                j += 1
            subArrSum[i] = 0

    # calculate total sum
    for i in range(0, len(subArrSum), 1):
        totalSum += subArrSum[i]

    # return totalSum
    return totalSum


# Drivers code
if __name__ == '__main__':
    arr = [4,10,5,2,2]
    n = len(arr)
    print(findSubarraySum(arr, n))

# This code is contributed by
# Sahil_Shelangia
