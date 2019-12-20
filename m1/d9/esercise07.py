"""
二分查找
"""
def binary_search(list_order,number):
    left_index = 0
    right_index = len(list_order)-1
    while left_index <= right_index:
        binary_index = left_index + right_index
        if list_order[binary_index] < number:
            left_index = binary_index + 1
        elif list_order[binary_index] > number:
            right_index = binary_index - 1
        else:
            return binary_index


print(binary_search([1,2,6,8,9],1))