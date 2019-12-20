file = open('file1','r')
# file.seek(-20,2)
print(file.readlines()[-1].split('.')[0])
file.close()