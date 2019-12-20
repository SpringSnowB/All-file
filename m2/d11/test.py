import re

f = open('./test')
list_post = []
data = f.read().split('\n\n')
print(data)
for i in data:
    print(i)
    post = re.search(r'^\S+',i).group()
    addr = re.search(r'(\d+\.){3}\d|Unknown+',i).group()
    print(post+':'+addr)
    # list_post.append(post)
# print(list_post)

# l = re.search(r'\S+','sihq23789r hodwoieh9832')
# print(l.group())