from data_structs.stack import Stack

def infix_to_prefix(infix_expr):
    print(infix_expr)
    prec = {
        '^': 4,
        '*': 3,
        '/': 3,
        '+': 2,
        '-': 2,
        ')': 1
    }
    chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    op_stack = Stack()
    prefix_list = []
    token_list = infix_expr.split()
    token_list.reverse()

    for token in token_list:
        if (token in chars) or is_number(token):
            prefix_list.append(token)
        elif token == ')':
            op_stack.push(token)
        elif token == '(':
            top_token = op_stack.pop()

            while top_token != ')':
                prefix_list.append(top_token)
                top_token = op_stack.pop()
        else:
            while (not op_stack.is_empty()) and \
                (prec[op_stack.peek()] >= prec[token]):
                prefix_list.append(op_stack.pop())

            op_stack.push(token)

    while not op_stack.is_empty():
        prefix_list.append(op_stack.pop())

    prefix_list.reverse()
    return ' '.join(prefix_list)

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

# print(infix_to_prefix('( A + B ) * C'))
# print(infix_to_prefix('5 * 3 ^ ( 4 - 2 )'))
# print(infix_to_prefix('( A + B ) * C - ( D - E ) * ( F + G )'))
print(infix_to_prefix('A + ( ( B + C ) * ( D + E ) )'))
