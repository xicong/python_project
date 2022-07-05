from requests import get

url = 'https://app.sports.qq.com/tokyoOly/medalsList?from=h5'
r = get(url) # 请求数据
result = r.json() # 转为json
if result['code'] == 0:
    data = result['data']['data']['total'] # 数据筛选
    print('以金牌数量排序')
    print('国家/缩写           金牌/排名 银牌/排名 铜牌/排名 总/排名') # 数据说明
    for country in data: # 格式化输出各国数据
        print('{:\u3000<12}{:<10}{:<10}{:<10}{:<10}'.format(f"{country['nocName']}/{country['nocShortName']}", f"{country['gold']}/{country['nocGoldRank']}", f"{country['silver']}/{country['nocSilverRank']}", f"{country['bronze']}/{country['nocBronzeRank']}", f"{country['total']}/{country['nocRank']}"))
else: # 请求错误
    print('错误')
    print(r.text)
input('结束任务')