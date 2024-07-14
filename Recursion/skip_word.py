def skip_word(s,word):
    ans=''
    def helper(s,ans,i,j,word):
        if i==len(s) and j==len(word):
            return ans
        if i>=j and j!=len(word):
            if s[i] == word[j]:
                return helper(s, ans, i + 1, j + 1, word)
            else:
                ans = ans + ''.join(s[i])
                return helper(s, ans, i + 1, j, word)
        else:
            ans = ans + ''.join(s[i])
            return helper(s,ans,i+1,j,word)
    return helper(s,'',0,0,word)

s='krishnaapple'
word='apple'
print(skip_word(s,word))