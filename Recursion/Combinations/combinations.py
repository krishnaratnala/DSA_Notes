
'''
it returns list of combination elements

def combination(s):
    ans = []
    def helper(p, up):
        if len(up)==0:
            if p!='':
              ans.append(p)
            return
        ch = up[0]
        helper(p + ch, up[1:])
        helper(p, up[1:])

    helper('', s)
    return ans


s = 'abc'
print(combination(s))
time complexity is o(2^n)
'''
def combination(s):
    def helper(s,p,up):
        if len(up)==0:
            if p!="":
                print(p)
                acc=''.join(str(ord(p))for p in p)
                '''
                ascc=[''.join(str(ord(p)) for p in p]
                the above logic concet the ascci values print in the form of list
                '''
                '''
                    assc=[ord(p) for p in p]
                    print(ascc)
                    it print list of ascci value
                '''
                print(acc)
            return
        ch=up[0]
        helper(s,p+ch,up[1:])
        helper(s,p,up[1:])
    helper(s,'',s)
    return
s='abc'
combination(s)
'''
it is printing the the combination of stirngs
'''