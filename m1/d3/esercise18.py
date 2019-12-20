"""
录入年份，是润年day赋值为29,否则赋值29
"""
year = int(input("请输入年份："))
#不建议使用真值表达式
day = 29 if year % 4 == 0 and year % 100 != 0 or year % 400 == 0 else 28
print(day)