from  lxml import etree


#只能够读取xml文件
html=etree.parse("./v30.html")

rst = etree.tostring(html,pretty_print=True)
print(rst)

