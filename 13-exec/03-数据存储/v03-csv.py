'''
csv()逗号分隔符
csv文件由任意的数据记录组成
记录间以某种换行符分割,每行记录由换行符组成
'''

import csv
headers = ['ID','UserName','Age','Country']
rows = [
    (1001,'dana',18,'Beijing'),
    (1002,'laoban',28,'Chengdu'),
    (1003,'yitengjun','Nan','Jinan'),
]

with open('test.csv','w') as f:
    f_csv = csv.writer(f)
    f_csv.writerow(headers)
    f_csv.writerows(rows)