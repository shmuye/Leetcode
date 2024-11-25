def frequency_sort(s):
    sDict = {}
    res = ''
    for ch in s:
        if ch in sDict:
            sDict[ch] += 1
        else:
            sDict[ch] = 1
    sorted_by_keys = dict(sorted(sDict.items(),key = lambda item: item[1],reverse=True))
    for ch in sorted_by_keys:
        res += ch*sorted_by_keys[ch]
    return res
s = 'tree'
print(frequency_sort(s))