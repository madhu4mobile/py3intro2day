
import os

a_var = 42
b_var = 3.1415
c_var = 'Hello'


def do_stuff():
    print("In do_stuff")


symbols = globals()

key = None
val = None

for key, val in symbols.items():
    print(f'{key} = {val}')
