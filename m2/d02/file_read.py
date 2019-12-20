f = open('/home/tarena/examples.desktop')
# while True:
#     s = f.read(100)
#     if not s:
#         break
#     print(s,end="")

read_line = f.readline(12)
print(read_line)
read_lines = f.readlines(25)#字符到哪行，就读取到哪行
print(read_lines)
#迭代特性
for i in f:
    print(i)

f.close()
