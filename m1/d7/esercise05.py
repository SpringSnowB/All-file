"""
比较大小
"""
list01 = [12,3,123,45,156,76,534]
for i in range(len(list01)-1):   #最后一个不用比，在前面已经比过了
    for j in range(i+1,len(list01)):
        if list01[i] > list01[j]:
            list01[i],list01[j] = list01[j],list01[i]
print(list01)


