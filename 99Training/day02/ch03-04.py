op_codes = {
    '+': lambda a, b: int(a) + int(b),
    '-': lambda a, b: int(a) - int(b),
    '*': lambda a, b: int(a) * int(b),
    '/': lambda a, b: int(a) / int(b)
}

exp = input("Enter an expression (similar to 4 * 23) : ")

num1, op, num2 = exp.split()

func = op_codes[op]
result = func(num1, num2)

print(result)
