"""
列表推导式
"""
names = ['zwj','zm','xz']
rooms = [101,102,103]
dict_name = {name:len(name) for name in names}   #列表转换成字典
print(dict_name)


#如何从多个列表中取出数据
#dict_name_room = {names[i]:rooms[i] for i in range(len(names))}
dict_name_room ={ name:room for name,room in zip(names,rooms)}  #两个列表转换成字典
print(dict_name_room)

#键值互换
dict_room_name = {v:k for k,v in zip(names,rooms)}
#dict_room_name = {v:k for k,v in dict_name_room.items()}
#如果有相同的值，会出现遗漏  价值在于互换后，根据键找值等同于互换前根据值找键

print(dict_room_name)