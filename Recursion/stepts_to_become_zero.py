
def steps_of_zeros(n):
    step = 0
    return helper(n, step)
def helper(n, step):
    if n == 0:
        return step
    if n % 2 == 0:
        return helper(n // 2, step + 1)
    return helper(n-1,step+1)

n =8
print(steps_of_zeros(n))

'''
 def numberOfSteps(num: int) -> int:
     if num == 0:
         return 0
     return  1 +numberOfSteps(num - 1 if num & 1 else num >> 1)'''