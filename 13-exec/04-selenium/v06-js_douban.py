'''
selenium的滚动
'''

from selenium import webdriver

driver = webdriver.PhantomJS()
driver.get('http://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=index&fr=&hs=0&xthttps=000000&sf=1&fmq=&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&word=%E8%8A%B1%E8%BE%B9&f=3&oq=hua&rsp=7')
driver.implicitly_wait(2)
driver.save_screenshot('./v06/image_start.png')

# 向下滚动到页面底部
js = 'document.body.scrollTop=10000'
driver.execute_script(js)
driver.implicitly_wait(2)
driver.save_screenshot('./v06/image_move.png')

driver.quit()