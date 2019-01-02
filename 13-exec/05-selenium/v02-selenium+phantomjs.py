'''
动态html
JS      一般嵌入在多媒体文件中,网页游戏
JQ      在源代码中包含jquery文件中
        <script type="text/javascript" src="https://....../jquery-1.11.1.min.js?v=34234></script>"

ajax    异步加载

DHTML   类似于ajax     动态html


如何解决这类页面的数据抓取
    1.直接从JS中采集内容(费事费力)
    2.利用python第三方库直接运行js
    3.selemium+phantomJS逆向工程


selemium
    是web的自动化测试工具
    下载地址:https://pypi.org/simple/selenium/
    参考文档:

phantomJS
    给予webkit的为界面浏览器
    selemium + phantomJS

'''
# 导入webdriver
from selenium import webdriver
import time
# 若想调用键盘按键需要引入keys包
from selenium.webdriver.common.keys import Keys

# 创建浏览器对象(如何没有放在bin文件下,则要指定具体路径executable_path="xxx")
driver = webdriver.PhantomJS()

# get方法
driver.get('https://www.baidu.com')

# 生成当前页面快照并保存
# driver.save_screenshot('./v02/baidu.png')

# print(driver.title)
'''
实现输入框输入内容,并点击百度一下,然后将搜索页截屏
'''

# 模拟百度搜索
# id = 'kw'输入框
driver.find_element_by_id('kw').send_keys(u'美女')
# id = 'su'百度一下按钮
# driver.find_element_by_id("su").click()
# 模拟回车
driver.find_element_by_id('kw').send_keys(Keys.ENTER)
# 等待页面响应
time.sleep(1)

# driver.save_screenshot('v02/girl.png')

# 打印当前页面源码
# print(driver.page_source)

# 获取当前页的cookie
# print(driver.get_cookies())

# 发送ctrl+x剪切输入框中的内容
driver.find_element_by_id('kw').send_keys(Keys.CONTROL,'a')
driver.find_element_by_id('kw').send_keys(Keys.CONTROL,'x')

# driver.save_screenshot('./v02/ctrl_x.png')

# 重新输入内容
driver.find_element_by_id('kw').send_keys('北京图灵学院')
# driver.save_screenshot('./v02/tlxy.png')

# 清空输入框
driver.find_element_by_id('kw').clear()
# driver.save_screenshot('./v02/clear.png')

# 获取当前url地址
print(driver.current_url)

driver.quit()