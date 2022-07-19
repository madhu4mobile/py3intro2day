#!/usr/bin/env python
#
"""
① treat spam and ham as a single iterable
② treat all elements of eggs as a single iterable
③ iterate over elements of fruits as long as length of current item > 4
④ iterate over elements of fruits as long as fruit does not start with 'k'
⑤ skip over elements of values as long as value is < 50, then iterate over all remaining elements
"""
from itertools import chain, takewhile, dropwhile

spam = ['alpha', 'beta', 'gamma']
ham = ['delta', 'epsilon', 'zeta']
for letter in chain(spam, ham):  # ①
    print(letter, end=' ')
print("\n")
eggs = [spam, ham]
for letter in chain.from_iterable(eggs):  # ②
    print(letter, end=' ')
print("\n")
fruits = ["pomegranate", "cherry", "apricot", "date", "apple",
          "lemon", "kiwi", "orange", "lime", "watermelon", "guava",
          "papaya", "fig", "pear", "banana", "tamarind", "persimmon",
          "elderberry", "peach", "blueberry", "lychee", "grape"]
for fruit in takewhile(lambda f: len(f) > 4, fruits):  # ③
    print(fruit, end=' ')
print("\n")
for fruit in takewhile(lambda f: f[0] != 'k', fruits):  # ④
    print(fruit, end=' ')
print("\n")
values = [5, 18, 22, 31, 44, 57, 59, 61, 66, 70, 72, 78, 90, 99]
for value in dropwhile(lambda f: f < 50, values):  # ⑤
    print(value, end=' ')
print("\n")
