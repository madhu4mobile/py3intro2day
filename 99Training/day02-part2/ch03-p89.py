"""
Grouping
• Groups consecutive elements by value
• Input must be sorted
The groupby() function groups consecutive elements of an iterable by value. As with sorted(), the value
my be determined by a key function. This is similar to sort -u or the uniq commands in Linux.
groupby() returns an iterable of subgroups, which can then be converted to a list or iterated over. Each
subgroup has a key, which is the common value, and an iterable of the values for that key.
For a more real-life example of grouping, see group_dates_by_week.py in the EXAMPLES folder.

① open file for reading
② create generator of all words, stripped of the trailing '\n'
③ create a groupby() object where the key is the first character in the word
④ make a dictionary where the key is the first character, and the value is the number of words that
start with that character; groupby groups all the words, then len() counts the number of words for
that character
⑤ sort the counts dictionary by value (i.e., number of words, not the letter itself) into a list of tuples
"""

# !/usr/bin/env python
from itertools import groupby

with open('../../resources/py3jpmcadv/DATA/words.txt') as words_in:  # ①
    all_words = (w.rstrip() for w in words_in)  # ②
g = groupby(all_words, key=lambda e: e[0])  # ③
counts = {letter: len(list(wlist)) for letter, wlist in g}  # ④
sorted_letters = sorted(counts.items(), key=lambda e: e[1], reverse=True)  # ⑤
for letter, count in sorted_letters:  # ⑥
    print(letter, count)
print()
print("Total words counted:", sum(counts.values()))  # ⑦
