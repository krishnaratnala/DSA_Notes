'''
def permutation(str):
    def helper(str,p,up):
        if len(up) == 0:
            print(p,end=' ,')
            return
        ch=up[0]
        for i in range(len(p)+1):
            new_helper=p[:i]+ch+p[i:]
            helper(str,new_helper,up[1:])
    helper(str,'',str)
str='123'
permutation(str)


it is printing the permutation result
'''

def permutation(str):
    result=[]
    def helper(str,p,up):
        if len(up) == 0:
            result.append(p)
            return
        ch=up[0]
        for i in range(len(p)+1):
            new_helper=p[:i]+ch+p[i:]
            helper(str,new_helper,up[1:])
    helper(str,'',str)
    return result
str='123'
print(permutation(str))

'''
it will the p value in to the result of list and it will return in form of result list
'''