'''
利用selenium执行js脚本
'''

from selenium import webdriver


driver = webdriver.PhantomJS()
driver.get('https://www.baidu.com')

# 让输入框有一个红色
js = 'var j = document.getElementById("kw");j.style.border="2px solid red"'

# 调用脚本
driver.execute_script(js)

# 截图
driver.implicitly_wait(2)
# driver.save_screenshot('./v06/red_baidu.png')

# 使用js隐藏图片
img = driver.find_element_by_xpath('//*[@id="lg"]/img')
driver.execute_script('$(arguments[0]).fadeOut()',img)
# driver.save_screenshot('./v06/nopic_baidu.png')

# 向下滚动到页面底部
driver.execute_script('$(".scroll_top").click(function(){$("html,body").animate({scrollTop:"0px"},800);})')
driver.save_screenshot('./v06/move_baidu.png')