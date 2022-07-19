
exp = input('Enter an expression - similar to  4 * 2 : ')
print(exp)

def add(a,b):
    return int(a) + int(b)

def sub(a,b):
    return int(a) - int(b)

def mutliply(a,b):
    return int(a) * int(b)

def divide(a,b):
    return int(a) / int(b)



num1, op, num2 = exp.split()

if op == '+':
    result = add(num1, num2)
elif op == '-':
    result = sub(num1, num2)
## and so on


### to make it simple, see ch03-04