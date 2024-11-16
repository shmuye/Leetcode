def strStr(haystack,needle):
    n = len(haystack)
    k = len(needle)
    for i in range(n - k + 1):
        j = 0 
        while j < k and haystack[i + j] == needle[j]:
            j += 1
        if j == k:
            return i
    return -1
    
haystack = 'leetcode'
needle = 'leeto'
print(strStr(haystack,needle))