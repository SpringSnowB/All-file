"""
1. 文件分离练习
   一个文件，文件名： "talk.txt"。在文件中保存着一些对话信息，格式如下
   老王： 吃了么
   老李： 没那，您呢？
​   老张: 您二位干什么呢
​   老李: 遛弯啊，刚买菜回来啊
   老张：是啊
​  通过程序将该文件进行分离，每个任务的说话内容，
  重新写入到一个新的文件中，文件以这个人的名字命名。
"""
file = open('./talk.txt','r')
for talk in file:
    name = talk.split('：')[0]
    print(name)
    talk_path = "./talk/"+name
    file_name = open(talk_path,'a')
    file_name.write(talk+'\n')
    file_name.close()
file.close()