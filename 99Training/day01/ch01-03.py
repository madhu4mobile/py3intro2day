import collections

count = collections.Counter()


with open('../resources/py3jpmcadv/DATA/breakfast.txt') as bf:
    for word in bf:
        word = word.strip()
        count[word] += 1

for key, cnt in count.items():
    print(key,cnt)