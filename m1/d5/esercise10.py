"""
将1970年到2050年之间所有润年存入列表
"""
# list_leap_year = []
# for year in range(1970,2051):
#     if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
#         list_leap_year.append(year)
#列表推导式：
list_leap_year = [year for year in range(1970,2051) if year% 4 == 0 and year % 100 != 0 or year % 400 == 0]
print(list_leap_year)
