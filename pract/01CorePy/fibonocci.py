# Program to display the Fibonacci sequence up to n-th term
from utils.ordinals import ordinal

nterms = int(input("How many terms? "))

# first two terms
n1, n2 = 0, 1
count = 0


# check if the number of terms is valid
if nterms <= 0:
    print("Please enter a positive integer")
# if there is only one term, return n1
elif nterms == 1:
    print("Fibonacci sequence upto", nterms, ":")
    print(n1)
# generate fibonacci sequence
else:
    print("Fibonacci sequence:")
    while count < nterms:
        # print('The '+ordinal(count+1)+' fibonacci number is : ',n1)
        print('The {} fibonacci number is :  {}'.format(str(ordinal(count+1)).ljust(5), str(n1).rjust(5)))
        # print('{}{}'.format(i.ljust(10), 'whatever'))
        nth = n1 + n2
        # update values
        n1 = n2
        n2 = nth
        count += 1
