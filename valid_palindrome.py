def isPalindrome(s):
    res = ''.join(char for char in s if char.isalnum()).upper()
    n = len(res)
    left = 0
    right = n - 1
    while left < right:
        if res[left] != res[right]:
            return False
        left += 1
        right -= 1
    return True
s = 'A man, a plan, a canal: Panama'
print(isPalindrome(s))