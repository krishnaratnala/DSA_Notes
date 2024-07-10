def count_zeros(n,count):
    if n==0:
        return count
    rem=n%10
    if rem==0:
        return count_zeros(n//10,count+1)
    else:
        return count_zeros(n//10,count)
n=202020
count=0
print(count_zeros(n,count))