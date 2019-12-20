"""
BMI:wight(kg)/hight(m)**2
"""
wight = float(input("请输入体重(kg):"))
hight = float(input("请输入身高(m):"))
bim = wight/hight**2
print(bim)
if bim < 18.5:
    print("体重过低，请好好吃饭哦！")
elif bim < 24:
    print("正常")
elif bim < 28:
    print("超重")
elif bim < 30:
    print("一度肥胖")
elif bim < 40:
    print("二度肥胖")
else:
    print("重度肥胖")