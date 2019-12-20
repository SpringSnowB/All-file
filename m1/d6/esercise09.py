"""

"""
# set_manage = {"曹操","刘备","孙权"}
# set_techology = {"曹操","刘备","张飞","关羽"}
# print(set_manage & set_techology)
# print(set_manage-set_techology)
# print(set_techology-set_manage)
# #print(set_manage ^ set_manage)
# print((set_manage-set_techology) | (set_techology - set_manage))
# print(len(set_manage | set_techology))
# print({"张飞"} < set_manage)
dict_person = {
    "经理": {"曹操","刘备","孙权"},
    "技术": {"曹操","刘备","张飞","关羽"}
}
print(dict_person["经理"] & dict_person["技术"])
print(dict_person["经理"] - dict_person["技术"])
print(dict_person["技术"] - dict_person["经理"])
print(dict_person["经理"] ^ dict_person["技术"])
print(len(dict_person["经理"] | dict_person["技术"]))
print({"张飞"} < dict_person["经理"])