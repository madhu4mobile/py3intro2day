a_var = 42
b_var = 3.1415
c_var = 'Hello'


def do_stuff():
    print("In do_stuff")


symbols = globals()

print(f'c_var = {c_var}')

symbols['c_var'] = 'Goodbye'

print(f'c_var = {c_var}')
