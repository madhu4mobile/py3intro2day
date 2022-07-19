#!/usr/bin/env python
#

'''
① count by tens starting at 0 forever
② without a check, will never stop
③ saner, using islice to get just the first 6 results
④ cycle over values in list forever (use islice to stop)
⑤ repeat value 10 times (default is repeat forever)
'''
from itertools import islice, count, cycle, repeat

for i in count(0, 10):
    if i > 50:
        break
print(i, end=' ')
print("\n")
for i in islice(count(0, 10), 6):
    print(i, end=' ')
print("\n")
giant = ['fee', 'fi', 'fo', 'fum']
for i in islice(cycle(giant), 10):
    print(i, end=' ')
print("\n")
for i in repeat('tick', 10):
    print(i, end=' ')
print("\n")
