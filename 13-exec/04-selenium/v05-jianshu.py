'''
爬取简述中的内容
https://www.jianshu.com/p/a32ef98c774f
'''

from  selenium import webdriver

driver = webdriver.PhantomJS()

driver.get('https://www.jianshu.com/p/a32ef98c774f')

driver.implicitly_wait(5)

author = driver.find_element_by_xpath('//div[@class="info"]/span/a').text
# print(author)
date = driver.find_element_by_xpath('//span[@class="publish-time"]').text

wordage = driver.find_element_by_xpath('//span[@class="wordage"]').text.split(' ')[-1]

views_count = driver.find_element_by_xpath('//span[@class="views-count"]').text.split(' ')[-1]

comments_count = driver.find_element_by_xpath('//span[@class="comments-count"]').text.split(' ')[-1]

likes_count = driver.find_element_by_xpath('//span[@class="likes-count"]').text.split(' ')[-1]

print(author,date,wordage,views_count,comments_count,likes_count)