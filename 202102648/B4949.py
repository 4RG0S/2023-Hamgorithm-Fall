while True:
    str_val = input()
    if str_val == '.':
        break

    stack = []
    result = True

    for el in str_val:
        if el in ['(', '[']:
            stack.append(el)
        elif el == ')':
            if not stack or stack[-1] == '[':
                result = False
                break
            elif stack[-1] == '(':
                stack.pop()
        elif el == ']':
            if not stack or stack[-1] == '(':
                result = False
                break
            elif stack[-1] == '[':
                stack.pop()

    if not stack and result:
        print('yes')
    else:
        print('no')
