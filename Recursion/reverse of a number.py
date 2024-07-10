import  math
def helper(n, digits):
    if (n%10==n) : return n
    rem=n%10
    return rem*int(math.pow(10,digits-1))+helper(n//10,digits-1)
def revers(n):
    digits=int(math.log10(n)+1)
    return (helper(n,digits))
n=1234
print(revers(n))
'''
def reverse(n):
    if n==0:
        :return
    rem=n%10
    n=n//10
    print(rem,end='')
    :return reverse(n)
'''