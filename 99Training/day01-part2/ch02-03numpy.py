import sys
import random
from pprint import pprint

import numpy as np

numbers = [random.randint(1, 30) for i in range(10)]

arr = np.array(numbers)

# pprint(dir(arr))

print(arr)
arr *= 10
print(arr)

arr1 = np.array([[1, 2, 3], [4, 5, 6]])
arr2 = np.array([[7, 8, 9], [10, 11, 12]])
#
# print(arr1)
# print(arr2)

arr3 = arr1 + arr2
print(arr3)

arr4 = arr1 * arr2
print(arr4)