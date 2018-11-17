'''
安装lxml
conda install lxml
'''
from lxml import etree

#创建一个残缺的文档,类似于html,使用etree来将内容补全
text='''
<div>
    <ul>
        <li class="item-0"> <a href="1.html"> first item </a></li>
        <li class="item-1"> <a href="2.html"> sec item </a></li>
        <li class="item-2"> <a href="3.html"> third item </a></li>
        <li class="item-3"> <a href="4.html"> four item </a></li>
        <li class="item-4"> <a href="5.html"> five item </a>
    </ul>
</div>
'''

html=etree.HTML(text)
s=etree.tostring(html)
print(s)