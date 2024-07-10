'''
def name(n):
    if n==0:
        return
    print("hello")
    name(n-1)
n=4
name(n)



def name(i,n):
    if i>n:
        return
    print("hello")
    name(i+1,n)
n=4
name(1,n)
'''


'''
print n to 1 values using only recursion
def value(n):
    if n==0:
        return
    print(n)
    value(n-1)
n=4
value(n)

def value(i,n):
    if (i>n):
        return
    value(i+1,n)
    print(i)
n=4
value(1,n)

def value(n):
    if n<=0:
        return n
    print(n)
    n-=1
    return(n)
n=4
value(n)
'''
'''
print values form 1 to n only using recursion 
def value(n):
    if n==0:
        return
    value(n-1)
    print(n)
n=4
value(n)


def value(i,n):
    if (i<1):
        return
    value(i-1,n)
    print(i)
n=4
value(n,n)
'''

''''
product of values 1 to n
def product_value(n):
    if n<=1:
        return n
    return product_value(n-1)*n
n=5
print(product_value(n))
'''
'''
sum fo values  n to1 

def sum_value(n):
    if n<=1:
        return n
    return sum_value(n-1)+n
n=4
print(sum_value(n))
'''


'''
sum of values  1 to n
def sum_value (n):
    if n==1:return  1
    return sum_value(n-1)+n
n=4
print(sum_value(n))
'''
