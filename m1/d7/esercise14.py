def season_to_month(season):
    """
    根据季度获取月份
    :param season: 获取季节
    :return: 季度
    """
    dict_season_month = {
        "春天":"1月2月3月",
        "夏天":"4月5月6月",
        "秋天":"7月8月9月",
        "冬天":"10月11月12月"
    }
    return dict_season_month[season]

print(season_to_month(input("请输入季节：")))
