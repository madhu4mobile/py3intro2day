# This is to find nth root of a given value
# This uses a utility 'ordinal_suffix' located in Ordinals.py
#  the inputs need to be the radicand, and root
from utils.ordinals import ordinal

def nth_root(radicand, n):
    return radicand ** (1 / n)

# def ordinal(value):
#     return str(value) + ordinal_suffix(value)

def display_nth_root(myRadicand, myNthFactor):
    # the received user values are always strings. They have to be converted to int to make the operation
    root = nth_root(int(myRadicand), int(myNthFactor))
    message = "The  " + ordinal(myNthFactor) + " root of " \
              + str(myRadicand) + " is " + str(root)
    print(message)
    pass

# aim is to get inputs from user for radicand and nthfactor like 16, 4 and then to display the result
# to display n'th root of the given number taken from user.
myRadicand = input('Provide the radicand value : ')
myNthFactor = input('\nWhat root of the radicand ' + myRadicand + ' you wanted to see ? : ')

display_nth_root(myRadicand, myNthFactor)

if __name__ == '__main__':
    print("\ndunder name of the module:")
    print(__name__)
