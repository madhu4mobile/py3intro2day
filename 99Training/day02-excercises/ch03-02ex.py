"""
Exercise 3-2 (pres_by_state.py)
Using presidents.txt, print out a list of the number of presidents from each state.
TIP
Use map() + lambda to split lines from presidents.txt on the 7th field, then use groupby()
on that.
"""

#!/usr/bin/python

with open("../DATA/presidents.txt") as pres_in:
    count_of = {}

    for rec in pres_in:
        flds = rec.split(":")
        state = flds[6]
        if state in count_of:
            count_of[state] += 1
        else:
            count_of[state] = 1

for state, count in sorted(count_of.items()):
    print("%-16s %2d" % (state, count))