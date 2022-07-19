

import functools

data = [1, 2, 3, 4, 5]
data1 = [1,2]

def my_func(a, b):
    print(f"a = {a}, b = {b}")
    return a + b

def my_new_func(a,b):
    print(f'a = {a} b = {b} ')
    return a + b

result = functools.reduce(my_func,data)
print('result = ',result)

result2 = functools.reduce(my_new_func,data,100)
print('result2 = ',result2)

result3 = functools.reduce(my_new_func(a,b),data1)
print('result3 = ',result3)