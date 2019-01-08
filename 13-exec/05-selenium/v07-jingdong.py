'''
爬取京东商品,并保存到mongdb
打开京东,并搜索笔记本
'''


from selenium import webdriver
import pymongo
# expected_conditions 负责条件的出发
from selenium.webdriver.support import expected_conditions as EC
'''
WebDriverWait设置等待
selenium主要提供隐形等待
参数:driver, timeout, poll_frequency=POLL_FREQUENCY, ignored_exceptions=None
    driver:webdriver的实例
    timeout:超时时间,等待的最长时间(可以考虑隐性的等待时间)
    poll_frequency:调用until/until_not中的方法的间隔时间,默认0.5s
    ignored_exceptions:忽略异常,如果在until/until_not的过程中抛出元祖中的异常,则不中断代码,继续等待
                                如果排除元组外的异常,则终端代码,抛出异常
'''
from selenium.webdriver.support.ui import WebDriverWait
# 异常捕获
from selenium.common.exceptions import TimeoutException
# 选择器
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time


# 启动浏览器
browser = webdriver.PhantomJS()
wait = WebDriverWait(browser,50)

# 链接数据库
client = pymongo.MongoClient('127.0.0.1',27017)
db = client['jd_computer']
collection = db['computer']


def to_mongodb(data):
    # 数据存储
    try:
       collection.insert(data)
       print('插入成功~~~')
    except:
        print('插入失败!!!')


def search():
    '''
    在京东页面搜索笔记本,并执行一些页面点击功能
    :return: 最大页数
    '''
    browser.get('https://www.jd.com')
    try:
        # 查找搜索框和按钮
        inputs = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR,"#key")))
        submit = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"#search > div > div.form > button")))
        # print(input,submit)
        inputs[0].send_keys('笔记本')
        submit.click()

        # 查找笔记本按钮和销量按钮
        button1 = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'ul.J_valueList > li:nth-child(1) > a')))
        button1.click()
        button2 = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#J_filter > div.f-line.top > div.f-sort > a:nth-child(2)')))
        button2.click()

        # 获取总页数
        page = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR,'#J_bottomPage > span:nth-child(2) > em > b')))
        return  page[0].text
    except TimeoutException:
        search()

# 获取下一页
def next_page(page_num):
    try:
        # 滑动网页到底部,加载所有商品信息
        browser.execute_script("window.scrollTo(0,document.body.scrollHeight);")
        time.sleep(10)
        html = browser.page_source
        parse_html(html)
        while page_num == 101:
            exit()
        # 查找下一页按钮,并点击
        button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#J_bottomPage > span.p-num > a.pn-next > em')))
        button.click()
        browser.execute_script("window.scrollTo(0,document.body.scrollHeight);")
        wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '#J_goodsList > ul > li:nth-child(60)')))
        # 判断翻页是否成功
        wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, '#J_bottomPage > span.p-num > a.curr'), str(page_num)))
    except TimeoutException:
        return next_page(page_num)

# 解析页面
def parse_html(html):
    data = {}
    soup = BeautifulSoup(html,'lxml')
    good_infos = soup.select('.gl-item')
    # 查看当前商品数量
    quantity = str(len(good_infos))
    print(quantity)
    for info in good_infos:
        # 获取商品标题信息
        title = info.select('.p-name.p-name-type-2 a em')[0].text.strip()
        data['_id'] = title
        # print(title)
        # 价格
        price = info.select('.p-price i')[0].text.strip()
        price = int(float(price))
        data['price'] = price
        # 评论数
        commit = info.select('.p-commit strong')[0].text.strip().replace('条评价','')
        if '万' in commit:
            commit = int(float(commit.split('万')[0]))*10000
        else:
            commit = int(float(commit.split('+')[0]))
        data['commit'] = commit
        # 店铺属性,是否自营
        shop_property = info.select('.p-icons i')
        if len(shop_property)>=1:
            mess = shop_property[0].text.strip()
            if mess == '自营':
                data['shop_property']='自营'
            else:
                data['shop_property'] = '非自营'
        else:
            data['shop_property'] = '非自营'
        # print(title,price,commit)
        to_mongodb(data)
        print(data)
        print('---------------------------')


def main():
    total = int(search())
    print(total)
    # next_page(2)
    for i in range(2,total+2):
        time.sleep(10)
        print('---第{}页---'.format(i-1))
        next_page(i)

if __name__ == '__main__':
    main()