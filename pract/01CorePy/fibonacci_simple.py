from utils.ordinals import ordinal

nterms = int(input("How many terms? "))



def f(n):
    if n <= 2:
        return 1
    return f(n - 1) + f(n - 2)
    pass

print('\nThe {} fibonacci number is :  {}'.format(str(ordinal(nterms)).ljust(5), str(f(nterms)).rjust(5)))
