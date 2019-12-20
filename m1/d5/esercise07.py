"""
将英文语句按单词反转
"""
message = "How are you"
list_result = message.split(" ")
print(list_result)
result_list=" ".join(list_result[::-1])
print(result_list)

# message = [1,2,3,6,5,8]
# print(message)
# result = "".join(str(message))
# print(result)
# print(str(message))