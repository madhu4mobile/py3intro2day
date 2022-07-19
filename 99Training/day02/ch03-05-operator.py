import operator

op_codes = {
    '+': operator.add,   # operator.add is built in lambda
    '-': lambda a, b: int(a) - int(b),
    '*': lambda a, b: int(a) * int(b),
    '/': lambda a, b: int(a) / int(b)
}

exp = input("Enter an expression (similar to 4 * 23) : ")

num1, op, num2 = exp.split()

func = op_codes[op]
result = func(int(num1), int(num2))

print(result)
