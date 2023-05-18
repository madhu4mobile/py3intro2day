from collections import defaultdict

dd = defaultdict(lambda: 0)

dd['spam'] = 10
dd['eggs'] = 20

print(dd['spam'])
print(dd['eggs'])
print(dd['foo'])

print('=' * 60)

fruits = ["pomegranate", "cherry", "apricot", "date", "apple",
          "lemon", "kiwi", "orange", "lime", "watermelon", "guava",
          "papaya", "fig", "pear", "banana", "tamarind", "persimmon",
          "elderberry", "peach", "blueberry", "lychee", "grape"]

fruit_info = defaultdict(list)

for fruit in fruits:
    first_letter = fruit[0]  # reading first letetr of each fruit.
    fruit_info[first_letter].append(fruit)

for letter,fruit in sorted(fruit_info.items()):
    print(letter, fruit)
