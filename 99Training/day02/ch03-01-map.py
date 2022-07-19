"""
Fucnction tools
    map() - acts like likst comprehension
    reduce() -
They reduce side-effects ( prevents modifying data outside the function )

    function can be passed into other function.

"""

data = [1, 2, 3, 4, 5, 5, 6]

doubles = [ num * 2 for num in data]
print(doubles)

def double_it(num):
    print(f'Doubling {num} :', end=" ")   ## important way to print the next character to the same line
    return num * 2

def half_it(num):
    print(f'Makeing half of  {num} :', end=" ")   ## important way to print the next character to the same line
    return num / 2

doubled = map(double_it, data)

halved = map(half_it, data)


for double in doubled:
    print(double)

print('=====>Printing Halfs <=====')
for half in halved:
    print(half)