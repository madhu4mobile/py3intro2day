#!/usr/bin/env python
"""

@author: jstrick
Created on Wed Mar 20 23:34:17 2013

"""
import csv
import pickle
from collections import namedtuple

fields = 'term firstname lastname birthplace birthstate party'
President = namedtuple('President', fields)

presidents = []
with open('../DATA/presidents.csv') as presidents_in:
    rdr = csv.reader(presidents_in)
    for row in rdr:
        president = President(*row)
        presidents.append(president)

p = presidents[15]
print(p.firstname, p.lastname, p.party)

with open('potus.pic','wb') as POTUS:
    pickle.dump(presidents,POTUS)
