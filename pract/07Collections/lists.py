
"""
Negative indices:
    last element is at index -1
    r[len(r) -1 ] will be same as r[-1]

Slicing :
    syntaxL a_list[start:stop]  ( excluding stop index)
Memebership and non-membership test:
    31 in s
    78 not in s
del:
    removes an element from the list
    Syntax : del a_list[index]  OR del a_list[value]
reverse(),sort()

"""
s = [3, 13, 28, 31, 46, 563, 9375]

print(s[1:-1])  # to print omiting first and last eleemnts
print(s[2:]) # to pirnt starting the 3rd element till the last
print(s[:2]) # to print start to the second element ( stop will not include the number )

print(31 in s)
print(78 not in s)
d = [59, 1, 73, 22, 3]
d.sort(reverse=True)
print(d)
d.sort()
print(d)

