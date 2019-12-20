import os
print(os.path.getsize('file1'))
print(os.listdir('.'))
print(os.path.exists('file'))
print(os.path.isfile('file'))
os.remove('file')
print(os.path.exists('file'))