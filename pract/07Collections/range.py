
"""
Range is a sequence than collector

"""

print(range(5))

for i in range(5):
    print(i)

print(list(range(5,10)))
print(list(range(0,20,2)))

s = [0,1,4,6,13]
# for i in range(len(s)):
#     print(s[i])  # this method may work. But it is not a recommended way in python

# pythonic way
for v in s:
    print(v)  ## recommneded way in python

t = [6, 48, 492, 8833, 93753, 574833]
for p in enumerate(t):
    print(p)   ## to print value including position

for i, v in enumerate(t):
    print(f' i = {i}, v = {v} ')

