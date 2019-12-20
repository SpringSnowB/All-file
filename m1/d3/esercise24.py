"""
在终端中获取年龄，显示婴儿（0-1）儿童（2-13）
青少年（14-20）成年人（21-65） 老年人（66-150）那是不可能的（以上）
重复判断，直到年龄录入空停止
"""

while True:
    age = input("请输入年龄：")
    if age =="":
        break
    age = int(age)
    if age > 150 or age < 0:
        print("ERROE")
    elif 66 <= age:
        print("老年人")
    elif 21 <= age:
        print("成年人")
    elif 14 <= age:
        print("青少年")
    elif 2 <= age:
        print("少年")
    else:
        print("婴儿")