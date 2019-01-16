'''
爬取拉勾网,采用selemium

url
https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false
data = {
    first: false
    pn: 2
    kd: python
}
'''
import requests
import random
import pandas as pd

User_Agent_List = [
    'User-Agent:Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
    'User-Agent:Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
    'User-Agent:Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0',
    'User-Agent:Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
]

for page in range(1,2):
    data = {
        'first': 'false',
        'pn': page,
        'kd': 'python'
    }
    headers = {
        'User-Agent': random.choice(User_Agent_List),
        'Host': 'www.lagou.com',
        'Origin': 'https://www.lagou.com',
        'Referer': 'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput=',
        'Content-Length':str(len(data))
    }
    url = 'https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false'
    res = requests.post(url,data=data,headers = headers)
    # print(res.status_code)
    # print(res.text)
    # print(res.json())
    decodejson = res.json()
    data = decodejson['content']['positionResult']['result']
    # print(data)
    ls = []
    for item in data:
        companyId = item['companyId']
        companyFullName = item['companyFullName']
        workYear = item['workYear']
        education = item['education']
        city = item['city']
        salary = item['salary']
        # print(companyId,workYear,education,city,salary)
        ls.append([companyId,companyFullName,workYear,education,city,salary])
    # print(ls)

    df = pd.DataFrame(ls,columns=['companyId','companyFullName','workYear','education','city','salary'])
    print(df)
    df.to_csv('v01-lagou.csv',index=False,mode='a+',encoding='gbk')