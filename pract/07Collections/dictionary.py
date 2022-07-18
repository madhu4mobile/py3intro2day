
"""
Dictionary = { 'key' : 'value' }

"""

country_to_capital =    {   'United Kingdom' : 'London',
                            'Brazil' : 'Brasilia',
                            'Morocco' : 'Rabat',
                            'Swedan' : 'Stockholm'
                        }
"""
## now we are going to print the list with capital first by following loop
#### in the loop below, a dictionary is being created as {capital : country}
     where for country, capital
     
"""
for country, capital in country_to_capital.items() :
    print ('capital : ',  capital)
    print ('country : ',country)


capital_to_country = {capital: country for country, capital in country_to_capital.items()}
from pprint import pprint as pp

print (pp(capital_to_country))

"""
Rule :
        Dictionary comprehensions don't work directly on dict sources.
        Use dict.items() to get keys and values from dict sources.
"""

words = ["hi", "hello", "foxtrot", "hotel"]
## while replacing there are many 'h' but the last word 'hotel' will be left at the end, where one word 'f' stores 'foxtrot'
print({x[0] : x for x in words})

import os
import glob

file_sizes = {os.path.realpath(p) : os.stat(p).st_size for p in glob.glob('*.py')}

print(pp(file_sizes))
