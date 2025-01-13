def expression_checker(expression: str) -> bool:
    if not expression:
        return False
    count_brackets = 0
    for sign in expression:
        if sign == '(':
            count_brackets += 1
        elif sign == ')':
            count_brackets -= 1
        if count_brackets < 0:
            return False
    return count_brackets == 0 

    
def expression_corrector(expression:str) -> list:

    solutions = set()
    quene = [expression]
    processed = [expression]
    max_solution_length = -1

    while quene:
        
        analyzed_expression = quene.pop(0)

        if len(analyzed_expression) < max_solution_length:
            break

        if expression_checker(analyzed_expression):
            solutions.add(analyzed_expression)
            max_solution_length = len(analyzed_expression)

        if max_solution_length == -1:

            for i in range(len(analyzed_expression)):
                sign = analyzed_expression[i]

                if not sign in ['(', ')']:
                    continue

                candidate = analyzed_expression[0:i] + analyzed_expression[i+1:]
        
                if candidate not in processed:
                    quene.append(candidate)
                    processed.append(candidate)

    return solutions

def expressions_engine(expression):
    if expression_checker(expression):
        return [expression]
    else:
        return expression_corrector(expression)
    
if __name__ == '__main__':
    expression = '((a+b))+(c+d))'
    result = expressions_engine(expression)
    
