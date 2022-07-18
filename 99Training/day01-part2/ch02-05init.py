

class my_list:

    def __init__(self, *args):
        self._data = []
        self._data.extend(args)

    def __setitem__(self, key, value):
        if key < len(self._data):
            self._data[key] = value
        else:
            for i in range(len(self._data), key):
                self._data.append(None)
            self._data.append(value)

    def __str__(self):
        tmp = [ str(item) for item in self._data]
        return '[ ' + ' '.join(tmp) + ' ]'

data = my_list(1, 2, 3)

data[1] = 42
data[10] = 99


print(data)