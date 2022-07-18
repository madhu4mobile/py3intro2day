

"""
replacement fields {}

    ex :
    "{0} north {1} east ".format(59.7, 10.4)

"""
import datetime
import math

print("{0} north {1} east ".format(59.7, 10.4))
print("The age of {0} is {1} ".format('Jim',47))
print("The age of {} is {} ".format('Jim',47))   # when the indices are not provided, they will be assigned in order

print("---> When used with indices, the field references can be used more than once <----")
print("The age of {0} is {1}. {0}\'s birthday is on {2}.".format('Jack', 34, 'November 25th'))

print("Math constatnts: pi = {m.pi:.3f}, e = {m.e:.3f}".format(m=math))
value = 4 * 20
print('The value is {value}'.format(value=value))

"""
    From Python3.6, f-string literal is added
"""
print(f"one plus two is { 1 + 2}") # the value is evaluated and printed at run time
print(f"The value is {value}")
print(f"The current time is {datetime.datetime.now().isoformat()}")
print(f'Math constants with format : pi = {math.pi:.3f}, e = {math.e:.3f}')
