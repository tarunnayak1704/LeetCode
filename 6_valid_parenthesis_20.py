def isValid(s):
    """
    :type s: str
    :rtype: bool
    """
    # use stack data structure and hashmap
    
    # we are using stack which is a python list
    stack = []

    # mapping closed parenthesis to open parenthesis
    closeToOpen = {")":"(", "]":"[", "}":"{"}

    # building the stack and popping from it
    for c in s:
        if c in closeToOpen:
            if stack and stack[-1] == closeToOpen[c]:
                stack.pop()
            else:
                return False
        else:
            stack.append(c)
    return True if not stack else False

print(isValid('()'))
print(isValid('(){}[]'))
print(isValid('{({[]})]'))