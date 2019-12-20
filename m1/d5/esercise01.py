"""
在终端中录入所有学生的身高，如果录入空，则打印
倒序打印身高
打印最高max()
打印最低min()
打印平均 sum()/len()

"""
list_height = []
while True:
    height = input("请输入身高：")
    if height !="":
        list_height.append(float(height))
    else:
        #不建议使用切片倒序，如果数据特别多的话，新建列表占内存
        #for i in list_height[::-1]:
            #print(i)
        for i in range(len(list_height)-1,-1,-1):
            print(list_height[i])
        print("最高身高是："+str(max(list_height)))
        print("最低身高是："+str(min(list_height)))
        print("平均身高是："+str(sum(list_height)/len(list_height)))
        break

