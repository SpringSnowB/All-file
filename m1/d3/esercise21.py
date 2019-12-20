"""
一张纸的厚度是0.01毫米
计算对折对少次超高珠穆朗玛（8844.43m）
"""
count = 0
flag = 1e-5
while flag <= 8844.43:
    flag *= 2
    count += 1
print("需要对折"+str(count)+"次")