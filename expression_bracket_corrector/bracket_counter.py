def expression_checker(expression:str) -> bool:
    opening_bracket = 0
    closing_bracket = 0
    for sign in expression:
        if sign == '(':
            opening_bracket += 1
        elif sign == ')':
            closing_bracket += 1
        if closing_bracket > opening_bracket:
            return False
    if opening_bracket != closing_bracket:
        return False
    elif expression == '':
        return False
    else:
        return True
    
def expression_corrector(expression:str) -> list:
    split_expression = []
    new_expressions = []
    for sign in expression:
        split_expression.append(sign)
    for i in range(len(split_expression)):
        if split_expression[i] == '(' or split_expression[i] == ')':
            temp = split_expression[i]
            split_expression[i] = ''
            str_expression = ''.join(split_expression)
            is_new_expression_correct = expression_checker(str_expression)
            if is_new_expression_correct and str_expression not in new_expressions:
                new_expressions.append(str_expression)
            split_expression[i] = temp

    return new_expressions

def longest_expression_selector(list_of_expressions:list) -> list:
    max_len = 0
    longest_expressions = []
    for element in list_of_expressions:
        if len(element) > max_len:
            max_len = len(element)
    for element in list_of_expressions:
        if len(element) == max_len:
            longest_expressions.append(element)
    return longest_expressions

def find_longest_correct_expressions(expression):
    is_expression_correct = expression_checker(expression)
    if is_expression_correct:
        longest_corrected_expressions = []
        longest_corrected_expressions.append(expression)
    else:
        corrected_expressions = expression_corrector(expression)
        longest_corrected_expressions = longest_expression_selector(corrected_expressions)
    return longest_corrected_expressions

if __name__ == '__main__':
    expression = '((a+b))+(c+d))'
    result = find_longest_correct_expressions(expression)
    print(result)
    
