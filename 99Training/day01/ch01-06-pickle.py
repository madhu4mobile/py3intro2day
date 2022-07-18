import pickle
from pprint import pprint

import os
script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in

airports = {
    'RDU': 'Raleigh-Durham', 'IAD': 'Dulles', 'MGW': 'Morgantown',
    'EWR': 'Newark', 'LAX': 'Los Angeles', 'ORD': 'Chicago'
}
colors = [
    'red', 'blue', 'green', 'yellow', 'black',
    'white', 'orange', 'brown', 'purple'
]
values = [
    3 / 7, 1 / 9, 14.5
]
data = [
    colors,
    airports,
    values,
]

with open('../resources/py3jpmcadv/TEMP/pickled_data.pic', 'wb') as pic_out:
    pickle.dump(data, pic_out)
with open('../resources/py3jpmcadv/TEMP/pickled_data.pic', 'rb') as pic_in:
    pickled_data = pickle.load(pic_in)
pprint(pickled_data)
