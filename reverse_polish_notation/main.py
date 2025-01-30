operations = {
    '+': 1,
    '-': 1,
    '*': 2,
    '/': 2,
    '^': 3
    }

def rpn_converter(expression:str) -> str:

    if expression.count('(') != expression.count(')'):
        return 'Expression incorrect.'

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

    return rpn

def calculate_segment(arg1, arg2, operator):

    arg1, arg2 = float(arg1), float(arg2)

    if operator == '+':
        return arg1 + arg2
    elif operator == '-':
        return arg1 - arg2
    elif operator == '*':
        return arg1 * arg2
    elif operator == '/':
        return arg1 / arg2
    elif operator == '^':
        return arg1 ** arg2
    else:
        raise ValueError(f'Value {operator} is incorrect.')
    
def calculate_rpn_expression(expression):

    temp_expression = []

    for char in expression:
        
        if char in operations.keys():
            arg2 = temp_expression.pop()
            arg1 = temp_expression.pop()
            temp_expression.append(calculate_segment(arg1, arg2, char))
        else:
            temp_expression.append(char)

    return temp_expression[0]

if __name__ == '__main__':
    expression = '7+2*(3*4+6/3)'
    converted_expression = rpn_converter(expression)
    solved_expression = calculate_rpn_expression(converted_expression)
    print(f'Original expression is {expression}')
    print(f'Converted expression to RPN is {converted_expression}')
    print(f'Solved RPN expression is equal: {solved_expression}')

    
