"""
一个小球从100 米落下，每次弹回原高度一半
计算总共弹起来多少次（最小弹起来高度0.01m）
    整个过程经过多少米
"""
height = 100
s = 100
count = 0
while height/2 >=0.01:
    count +=1
    height /=2
    s += height*2
    print(height,count,s)