def isValid(s):
    temp = []
    opening = ['(','[','{']
    closing = [')',']','}']
    for ch in s:
        if ch in opening:
            temp.append(ch)
        elif ch in closing:
            if not temp:
                return False
            top = temp.pop()
            if (ch == ')' and top !='(') or\
               (ch == ']' and top != '[') or\
               (ch == '}' and top != '{'):
                return False
    return len(temp) == 0
s = '()[]{}'
if (isValid(s) == True):
    print('balanced')
else:
    print('not balanced')
