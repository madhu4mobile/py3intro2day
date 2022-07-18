from pprint import pprint
from sys import getsizeof
from array import array
import random

values = [random.randint(1, 30000) for i in range(1000)]
print(f'Size of integer list: {getsizeof(values)}\n')
for datatype in 'i', 'h', 'L', 'Q', 'd':
    data_array = array(datatype, values)
print(f'Size of {datatype} array: {getsizeof(data_array)} Contents:',
      data_array[:5], '...')
print()

numbers = [ random.randint(1, 300) for i in range(10)]

#pprint(numbers)

arr = array.array('i', numbers)

#print(dir(arr))
print(arr)




