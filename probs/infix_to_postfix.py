from data_structs.stack import Stack

# 5 * 3 ˆ ( 4 − 2 )

def complete_paren(symbol_string):
    s = Stack()
    balanced = True

    index = 0
    while index < len(symbol_string) and balanced:
        symbol = symbol_string[index]

        if symbol == '(':
            s.push(symbol)
        elif symbol == ')':
            if s.is_empty():
                balanced = False
            else:
                s.pop()

        index += 1

    if balanced and s.is_empty():
        return True
    else:
        return False

def check_valid(expr):
    if not complete_paren(expr):
        raise ValueError('Incomplete parenthesis')

def infix_to_postfix(infix_expr):
    check_valid(infix_expr)

    prec = {
        '^': 4,
        '*': 3,
        '/': 3,
        '+': 2,
        '-': 2,
        '(': 1
    }
    chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    op_stack = Stack()
    postfix_list = []
    token_list = infix_expr.split()

    for token in token_list:
        if (token in chars) or is_number(token):
            postfix_list.append(token)
        elif token == '(':
            op_stack.push(token)
        elif token == ')':
            top_token = op_stack.pop()

            while top_token != '(':
                postfix_list.append(top_token)
                top_token = op_stack.pop()
        else:
            while (not op_stack.is_empty()) and \
                (prec[op_stack.peek()] >= prec[token]):
                postfix_list.append(op_stack.pop())

            op_stack.push(token)

    while not op_stack.is_empty():
        postfix_list.append(op_stack.pop())

    return ' '.join(postfix_list)

def do_math(op, op1, op2):
    if op == "^":
        return op1 ** op2
    elif op == "*":
        return op1 * op2
    elif op == "/":
        return op1 / op2
    elif op == "+":
        return op1 + op2
    else:
        return op1 - op2

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

# print(infix_to_postfix('( A + B ) * C'))
# print(infix_to_postfix('5 * 3 ^ ( 4 - 2 )'))
print(infix_to_postfix('( A + B ) * C - ( D - E ) * ( F + G )'))

def postfix_eval(postfix_expr):
    operand_stack = Stack()
    token_list = postfix_expr.split()

    for token in token_list:
        if is_number(token):
            operand_stack.push(int(token))
        else:
            op2 = operand_stack.pop()
            op1 = operand_stack.pop()
            result = do_math(token, op1, op2)
            operand_stack.push(result)

    return operand_stack.pop()

# print(postfix_eval('5 3 4 2 - ^ *'))
