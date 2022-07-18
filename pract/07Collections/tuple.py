
'''
Tuple is a list that starts with paranteses. ()

we can access elements of tuple by its index like t[0] and t[2]

'''

t = ('Norway', 4.953, 3)

print('t[0] is :',t[0])
print('t[2] is :',t[2])

'''
Tuple new items can be added. And we can do mathematical operations like t * 3 and t + (33.463, 25e6)
'''
print( t*3)

for item in t:
    print(item)

# tuple can be nested
a = (('a','b'),(56,98),(93.2,45.89),(34e2,10e3))
print(a[3][1])

"""
When a single int is given as tupple, it will be termed as int as type.
But when a trailing comma separator is used, it will be treated as tupple
"""
h = (345)
g = (345, )
e = () # method to specify empty tuple
print("Type of h is {} \nType of g is {}\nType of e is {} ".format(type(h),type(g),type(e)))

"""
Commonly a tupple can be indicated without a paranthese as p = 1,1,1,4,6,19
type(p) = <class 'tuple'>
"""
def minmax(items):
    return min(items), max(items)

mySet1 = (35,29,49,87,21,9,67)
mySet2 = ([35,29,49,87,21,9,67])
print(minmax(mySet1))
print('Type of mySet1 :',type(mySet1))
print(minmax(mySet2))
print('Type of mySet2 :',type(mySet2))

"""
Unpacking tuple.
    Destructing operation that unpacks data structures into named references
"""
lower, upper = minmax([35,29,49,87,21,9,67])  # first value in return goes as lower and the next one as upper
print('lower --> : ', lower, ' upper --> : ',upper)

## Another example - with nested tuple

(a, (b, (c,d))) = ( 34, ( 'This is b', ( 92.3, False)))

print ('Values of a,b,c,d  in nested tuple are respectively : ', a,b,c,d)

"""
Tip to swap tuples
"""
x = 'first'
y = 'second'

x, y = y , x

print('after swapping x and y : ',x,y)

print('tuple("Cramshell") : ', tuple("Cramshell"))
print('5 in (3,5,17,257,43537) : ', 5 in (3,5,17,257,43537) )
