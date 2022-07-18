
from math import sqrt

def is_prime(x):
    if x < 2:
        return False
    #for i in range(2, int(sqrt(x)) + 1):
    for i in range(2, x):
        if (x % i) == 0:
            return False
        return True

print(is_prime(29))

print(is_prime(3420482048230483463249823474383473489473291))

print([x for x in range(129) if is_prime(x)])
