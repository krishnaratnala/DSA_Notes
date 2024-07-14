'''
import  math
def helper(n, digits):
    if (n%10==n):return n
    rem=n%10
    return rem*int(math.pow(10,digits-1))+helper(n//10,digits-1)
def palindrome(n):
    digits=int(math.log10(n)+1)
    return (n==helper(n,digits))
n=55255
print(palindrome(n))
'''


def helper(n, start, end):
    if start>=end:    return True
    if n[start]!=n[end]:return False
    return helper(n,start+1,end-1)


def palindrome(n):
    n=str(n)
    start=0
    end=len(n)-1
    return helper(n,start,end)
n=55255
print(palindrome(n))