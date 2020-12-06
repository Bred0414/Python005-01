# Author:Bred
# 第二周作业，智能手机热度排行前30名

import requests
from lxml import etree
import pandas as pd
from fake_useragent import UserAgent


def requests_get():
    ua = UserAgent(verify_ssl=False)
    header = {'user-agent': ua.random,
              'Referer': 'https://www.smzdm.com/'}

    url = 'https://www.smzdm.com/fenlei/zhinengshouji/'
    r = requests.get(url, headers=header)

    selector = etree.HTML(r.text)
    name_type = selector.xpath('//div[@class="z-feed-content "]/h5/a/text()')
    money = selector.xpath('//div[@class="z-highlight"]/a/text()')
    link = selector.xpath('//div[@class="z-feed-content "]/h5/a/@href')

    data = pd.DataFrame(index=[i for i in range(30)])
    data['商品名称'] = ''
    data['价格'] = ''
    data['连接'] = ''

    for i in range(30):
        data['商品名称'].loc[i] = name_type[i]
        data['价格'].loc[i] = money[i].strip().lstrip()
        data['连接'].loc[i] = link[i]
        if data['价格'].loc[i] == '':
            data['价格'].loc[i] = "商品优惠过期"

    data.to_excel('最新智能手机热度前30名.xlsx')


if __name__ == '__main__':
    requests_get()
