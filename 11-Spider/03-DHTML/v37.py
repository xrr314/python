from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

#尽量使用Chrome
driver = webdriver.Chrome()

url = "http://www.baidu.com"

driver.get(url)

print(driver.title)
text = driver.find_element_by_id('wrapper').text
print(text)
print(driver.title)

# 获得页面的快照
driver.save_screenshot('index.png')

#id='kw'的是百度的输入框
driver.find_element_by_id('kw').send_keys(u'大熊猫')
#id为'su'的搜索按钮,使用click来模拟点击
driver.find_element_by_id('su').click()

time.sleep(5)
driver.save_screenshot('daxiongmao.png')

#获取当前页面的cookie
print(driver.get_cookies())

#模拟输入两个按键 ctrl + a
driver.find_element_by_id('kw').send_keys(Keys.CONTROL, 'a')

#ctrl+x 剪切
driver.find_element_by_id('kw').send_keys(Keys.CONTROL, 'x')

driver.find_element_by_id('kw').send_keys(u'航空母舰')
driver.save_screenshot('hangmu.png')

driver.find_element_by_id('su').send_keys(Keys.RETURN)

time.sleep(5)
driver.save_screenshot('hangmu2.png')

#清空输入框
driver.find_element_by_id('kw').clear()
driver.save_screenshot('clear.png')

#关闭浏览器
driver.quit()