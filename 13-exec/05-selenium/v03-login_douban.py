'''
模拟豆瓣登陆
implicitly_wait():隐式等待
    当使用了隐士等待执行测试的时候，如果 WebDriver没有在 DOM中找到元素，将继续等待，
        超出设定时间后则抛出找不到元素的异常换句话说，当查找元素或元素并没有立即出现的时候，
        隐式等待将等待一段时间再查找 DOM，默认的时间是0
    一旦设置了隐式等待，则它存在整个 WebDriver 对象实例的声明周期中，
        隐式的等到会让一个正常响应的应用的测试变慢，
    它将会在寻找每个元素的时候都进行等待，这样会增加整个测试执行的时间。

显式等待
    就是明确的要等到某个元素的出现或者是某个元素的可点击等条件,等不到,就一直等,
        除非在规定的时间之内都没找到,那么就跳出Exception.如:
    newWebDriverWait(driver,15).until(
                  ExpectedConditions.presenceOfElementLocated(By.cssSelector("css locator")));
    这里,15是要等待的秒数.如果没有满足until()方法中的条件,就会始终在这里wait 15秒,
        依然找不到,就抛出异常.
'''

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.PhantomJS()

driver.get('https://www.douban.com')
# 等待,不同于
driver.implicitly_wait(5)
driver.save_screenshot('./v03/login.png')

driver.find_element_by_id('form_email').send_keys('15080334894')
driver.find_element_by_id('form_password').send_keys('xrr940314')
driver.find_element_by_class_name('bn-submit').click()
driver.save_screenshot('./v03/success.png')