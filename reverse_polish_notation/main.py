operations = {
    '+': 1,
    '-': 1,
    '*': 2,
    '/': 2,
    '^': 3
}

stack = []
expression = '7+2*(3*4+6/3)'
rpn = ''

for char in expression:
    if char == '(':
        stack.append(char)
    elif char == ')':
        stack_top = stack.pop()
        while stack_top != '(':
            rpn += stack_top
            stack_top = stack.pop()
    elif char in operations.keys():
        while len(stack) > 0 and stack[-1] != '(' and operations[stack[-1]] >= operations[char]:
            rpn += stack.pop()
        stack.append(char)
    else:
        rpn += char
else:
    while len(stack) > 0:
        rpn += stack.pop()

print(rpn)
