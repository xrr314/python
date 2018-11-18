# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json

class E15MeijuPipeline(object):
    def process_item(self, item, spider):
        return item


class MeijuPipeline(object):

    def __init__(self):
        self.file=open('meiju.json','wb')
    '''
    此方法必须被实现
    用来具体处理item内容
    且必须返回一个tiem
    '''
    # 这个案例中不需要对item进行什么处理

    def process_item(self,item,spider):
        with open('meiju.json','a')  as f:
            json.dump(dict(item),f,)

        return item