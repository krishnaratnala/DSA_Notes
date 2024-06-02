def search_string(str,target_char):
    n=len(str)
    if n<0:
        return -1
    for i in range(n):
        if str[i]==target_char:
            return str[i]
    return -1
str="krishna"
target_char="i"
print(search_string(str,target_char))


here 