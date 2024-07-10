def skip_a(s):
    ans = ''
    def helper(s, ans, i):
        if i == len(s):
            return ans
        if s[i] != 'a':
            ans = ans + s[i]
        return helper(s, ans, i + 1)

    return helper(s, ans, 0)

s = 'aaccbb'
print(skip_a(s))
