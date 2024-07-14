def dice(arr, target):
    result = []

    def helper(path, remaining, start):
        if remaining == 0:
            result.append(path)
            return
        for i in range(start, len(arr)):
            if arr[i] <= remaining:
                helper(path + [arr[i]], remaining - arr[i], i)

    helper([], target, 0)

    def generator():
        for combination in result:
            yield combination

    return generator()
arr = [1, 2, 3, 4, 5, 6]
target = 4
gen = dice(arr, target)
print(list(gen))  # Print all generated combinations
