from  lxml import etree


#只能够读取xml文件
html=etree.parse('./v30.html')

#print(type(html))

rst=html.xpath('//book')

rst = html.xpath('//book[@category="sport"]/year')
rst=rst[0]
print(type(rst))
print(rst)

print(rst.tag)
print(rst.text)