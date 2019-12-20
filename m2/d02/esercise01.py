words = open('dict.txt')
word = input("请输入单词：")

for line in words:
    w = line.split(' ')[0]
    if w>word:
        print("未找到该单词")
        break
    elif word==w:
        print(line)
        break
else:
    print("未找到该单词")



# for line in words:
#     if line.startswith(word):
#         print(line)
#         break
# else:
#     print("not find")