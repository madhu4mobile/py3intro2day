#!/usr/bin/env python
import pickle
from pprint import pprint

# <1>
airports = {
    'RDU': 'Raleigh-Durham', 'IAD': 'Dulles', 'MGW': 'Morgantown',
    'EWR': 'Newark', 'LAX': 'Los Angeles', 'ORD': 'Chicago'
}

colors = [
    'red', 'blue', 'green', 'yellow', 'black',
    'white', 'orange', 'brown', 'purple'
]

values = [
    3/7, 1/9, 14.5
]

data = [  # <2>
    colors,
    airports,
    values,
]

with open('../TEMP/pickled_data.pic', 'wb') as pic_out:  # <3>
    pickle.dump(data, pic_out)  # <4>

with open('../TEMP/pickled_data.pic', 'rb') as pic_in:  # <5>
    pickled_data = pickle.load(pic_in)  # <6>

pprint(pickled_data)  # <7>
