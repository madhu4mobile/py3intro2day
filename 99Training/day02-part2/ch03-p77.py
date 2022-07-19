class my_range:

    def __init__(self, stop, step=1):
        self._curr = 0
        self._stop = stop
        self._step = step

    def __iter__(self):
        return self

    def __next__(self):
        if self._curr >= self._stop:
            raise StopIteration
        self._curr += self._step
        return self._curr
print('[ ',end = '')
for i in range(10):
    print(i, end = ', ')
print(']')

print('[ ',end = '')
for j in my_range(10, 1):

    print(j, end = ', ')
print(']')
