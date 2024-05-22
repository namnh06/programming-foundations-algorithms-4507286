# Example file for Programming Foundations: Algorithms by Joe Marini
# Use a stack to see if a programming statement is balanced


def is_balanced(thestr):
    stack = []
    open_parentheses = ['(', '{', '[']
    close_parentheses = [')', '}', ']']
    for i in thestr:
        if i in open_parentheses:
            stack.append(i)

        if i in close_parentheses:
            if len(stack) < 1:
                return False
            test = stack.pop()
            if test == '(' and i != ')':
                return False
            if test == '{' and i != '}':
                return False
            if test == '[' and i != ']':
                return False
    
    if len(stack) > 0:
        return False
    return True

test_statements = [
    "(}",
    "print('Hello World!')",
    "a(x[i]) == b(x[i])",
    "{c for c in a(x)}",
    "Hello!)",
    "(This is not [balanced)",
    "{{{[[(())]}}",
    "(",
    "}"
]

for statement in test_statements:
    print(f'{statement} balanced: {is_balanced(statement)}')
