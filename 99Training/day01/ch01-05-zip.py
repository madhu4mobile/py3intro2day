
import zipfile

zf = zipfile.ZipFile('../resources/py3jpmcadv/DATA/alice.zip')

for item in zf.filelist:
    print(item)

data = zf.read('mary.txt')
print(data) # comes as binary
print(data.decode()) ## applies the