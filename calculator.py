import math
import re
import operator

operators = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
    '^': operator.pow
}

functions = {
    'sin': math.sin,
    'cos': math.cos,
    'tan': math.tan,
    'log': math.log10,
    'ln': math.log,
    'sqrt': math.sqrt,
    'exp': math.exp
}


constants = {
    'pi': math.pi,
    'e': math.e
}

precedence = {
    '+': 1,
    '-': 1,
    '*': 2,
    '/': 2,
    '^': 3
}

def tokenize(expression):
    pattern = r'\d+\.?\d*(?:e[+-]?\d+)?|[a-zA-Z]+|[+\*/^()-]'
    return re.findall(pattern, expression)

def infix_to_postfix(tokens):
    output = []
    stack = []
    for token in tokens:
        if token in operators:
            while (stack and stack[-1] in operators and
                   precedence[stack[-1]] >= precedence[token]):
                output.append(stack.pop())
            stack.append(token)
        elif token in functions:
            stack.append(token)
        elif token in constants or token == "ans":
            output.append(token)
        elif token == '(':
            stack.append(token)
        elif token == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            if stack and stack[-1] == '(':
                stack.pop()
            if stack and stack[-1] in functions:
                output.append(stack.pop())
        else:
            if re.match(r'\d+\.?\d*(?:e[+-]?\d+)?', token):
                output.append(token)
            else:
                raise ValueError("Invalid token: " + token)
    while stack:
        if stack[-1] == '(':
            raise ValueError("Mismatched parentheses")
        output.append(stack.pop())
    return output

def evaluate_postfix(postfix, last_result):
    stack = []
    for token in postfix:
        if token == "ans":
            stack.append(last_result)
        elif token in constants:
            stack.append(constants[token])
        elif token in functions:
            if len(stack) < 1:
                raise ValueError("Invalid expression")
            arg = stack.pop()
            stack.append(functions[token](arg))
        elif token in operators:
            if len(stack) < 2:
                raise ValueError("Invalid expression")
            arg2 = stack.pop()
            arg1 = stack.pop()
            stack.append(operators[token](arg1, arg2))
        else:
            try:
                stack.append(float(token))
            except ValueError:
                raise ValueError("Invalid token: " + token)
    if len(stack) != 1:
        raise ValueError("Invalid expression")
    return stack[0]

def calculate(expression, last_result):
    expression = expression.replace(' ', '')
    tokens = tokenize(expression)
    if ''.join(tokens) != expression:
        raise ValueError("Invalid characters in expression")
    postfix = infix_to_postfix(tokens)
    return evaluate_postfix(postfix, last_result)
last_result = 0
print("Scientific Calculator. Type 'quit' to exit.")
while True:
    expression = input("Enter expression: ").strip()
    if expression.lower() == 'quit':
        break
    try:
        result = calculate(expression, last_result)
        print("Result:", result)
        last_result = result
    except ZeroDivisionError:
        print("Error: Division by zero")
    except ValueError as e:
        print("Error:", e)
    except Exception as e:
        print("Error:", e)