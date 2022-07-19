
"""
Exercise 3-1 (sum_of_values.py)
Read in the data from float_values.txt and print out the sum of all values. Do this with functional tools
– there should be no explicit loops in your code.
TIP
use reduce() + operator.add on the file object.
"""


import operator
from functools import reduce

with open('../../resources/py3jpmcadv/DATA/float_values.txt') as fv_in:
    sum = reduce(operator.add, map(float, fv_in))

print("{:.2f}".format(sum))

# or, for the truly functional experience:

print(reduce(operator.add, map(float, open('../../resources/py3jpmcadv/DATA/float_values.txt'))))
