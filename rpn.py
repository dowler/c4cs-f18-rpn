#!/usr/bin/env python3

import operator, math

def percentage(a, b):
    return (a / float(b)) * 100

def exponent(a, b):
    return operator.pow(a, b)

def intdiv(a, b):
    return operator.floordiv(a, b)

def andfunc(a, b):
    return operator.and_(a, b)

def orfunc(a, b):
    return operator.or_(a, b)

def notfunc(a, b):
    return operator.xor(a, b)

 
operators = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
    '%': percentage,
    '^': exponent,
    '//': intdiv,
    '&': andfunc,
    '|': orfunc,
    '!': notfunc,

}

def calculate(myarg):
    stack = list()
    for token in myarg.split():
        try:
            if token == 'pi':
                token = math.pi
            elif token == 'e':
                token = math.e
            elif token == 'sin':
               result = math.sin(stack.pop())
                stack.append(result)
                break
            elif token == 'cos':
                result = math.cos(stack.pop())
                stack.append(result)
                break
            else:
                token = int(token)
    
            stack.append(token)
        except ValueError:
            function = operators[token]
            arg2 = stack.pop()
            arg1 = stack.pop()
            result = function(arg1, arg2)
            stack.append(result)
        print(stack)
    if len(stack) != 1:
        raise TypeError("Too many parameters")
    return stack.pop()

def main():
    while True:
        result = calculate(input("rpn calc> "))
        print("Result: ", result)

if __name__ == '__main__':
    main()
