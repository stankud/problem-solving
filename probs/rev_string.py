from data_structs.stack import Stack

def rev_string(string):
    s = Stack()

    for l in string:
        s.push(l)

    rev_string = ''
    while not s.is_empty():
        rev_string += s.pop()

    return rev_string

string1 = 'information'
print(f'reverse of {string1} is {rev_string(string1)}')
