
"""
Topics being covered :
    ch01 - Idiomatic data handling


"""
import copy

data1 = [ [1, 2, 3], [4, 5, 6] ]
d1 = list(data1)
d1[0].append(99)
print(data1)

arr = [['foo', 'bar', 'baz'],[1,2,3]]
arr1 = arr
arr2 = copy.copy(arr)
arr3 = copy.deepcopy(arr)

arr2.append("item1")
arr3.append("item2")

print(id(arr),id(arr1),id(arr2),id(arr3))

print(arr)
print(arr1)
print(arr2)
print(arr3)

## ordered dictionary


# ## the arr and arr2 are different objects.
# print(f'arr = {id(arr):#x}')
# print(f'arr2 = {id(arr2):#x}')
#
# arr.append('blah')
# print(id(arr))
# print(id(arr2))
# print(arr,arr2)
# print(f'arr = {id(arr):#x}')
# print(f'arr2 = {id(arr2):#x}')