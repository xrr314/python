import  requests
import  os,random
from lxml import etree

user_agent_list = [
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36',
        'Mozilla/5.0 (Android; Mobile; rv:14.0) Gecko/14.0 Firefox/14.0',
        'Mozilla/5.0 (iPad; CPU OS 5_0 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9A334 Safari/7534.48.3'
    ]
if __name__ == '__main__':
    headers = {
        'User-Agent': random.choice(user_agent_list),
        'Referer': 'https://www.mzitu.com/'
    }
    url = 'https://i.meizitu.net/2018/11/27a01.jpg'
    rsp = requests.get(url,headers=headers )
    # print(rsp)
    with open('27a01.jpg','wb') as f:
        # print(rsp.content)
        f.write(rsp.content)
        f.close()