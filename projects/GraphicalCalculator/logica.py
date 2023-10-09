import re

numbers = []
operators = []


def reset_lists():
    global numbers, operators
    numbers = []
    operators = []


def evaluate_expression(expression):
    expression = expression.replace(" ", "")
    tokens = re.findall(r"[\d.]+|[-+*/^]", expression)
    numbers = []
    operators = []
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}

    for token in tokens:
        if token.replace(".", "").isdigit():  # Verifique se é um número (int ou float)
            numbers.append(float(token))
        elif token in "+-*/^":
            while (operators and operators[-1] in "+-*/^" and precedence[token] <= precedence[operators[-1]]):
                operator = operators.pop()
                num1 = numbers.pop()
                num2 = numbers.pop()
                if operator == '+':
                    numbers.append(num2 + num1)
                elif operator == '-':
                    numbers.append(num2 - num1)
                elif operator == '*':
                    numbers.append(num2 * num1)
                elif operator == "/":
                    numbers.append(num2 / num1)
                elif operator == "^":
                    numbers.append(num2 ** num1)
            operators.append(token)
        else:
            raise ValueError("Token inválido: {}".format(token))

    while operators:
        operator = operators.pop()
        num1 = numbers.pop()
        num2 = numbers.pop()
        if operator == '+':
            numbers.append(num2 + num1)
        elif operator == '-':
            numbers.append(num2 - num1)
        elif operator == '*':
            numbers.append(num2 * num1)
        elif operator == "/":
            numbers.append(num2 / num1)
        elif operator == "^":
            numbers.append(num2 ** num1)

    if len(numbers) == 1 and not operators:
        return numbers[0]
    else:
        raise ValueError("Expressão inválida")
