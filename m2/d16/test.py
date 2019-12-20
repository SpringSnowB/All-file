file = open('./dict.txt')
word_dict={}
data_list = []
while True:
    data = file.readline()
    if not data:
        break
    data_list.append(data.split('\n'))

print(data_list)
print(len(data_list))


    # word = data[0].split(' ',1)[0]
    # mean = data[0].split(' ',1)[1]
    # print(word+'----------')
    # print(mean)
    # if not data:
    #     break


print(len(word_dict))