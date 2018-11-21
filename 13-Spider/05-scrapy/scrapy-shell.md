# scrapy-shell
- http://segmentfault.com/a/1190000013199636?utm_source=tag-newest
- shell
- 启动
    - linux: ctrl+alt+T,打开终端,进入环境,然后输入scrapy shell "url:xxx"
    - windows:打开anaconda prompt ,然后输入scrapy shell "url:xxx"
    - 启动之后自动下载指定的URL网页
    - 下载完成之后,url的内容会被保存在reponse的变量中,如果需要,我们需要调用response
- response
    - 爬取到的两日恶龙保存在response中
    - response.body是网页的代码
    - response.headers是返回的http头信息
        可以使用遍历for h in response.headers:回车,tab缩进print(h),两次回车
    - response.xpath()允许使用xpath语法选择内容
    - response.css()允许使用

- selector
    - 选择器,允许用户使用选择器来选择自己想要的内容
    - response.selector.xpath:response.xpath是selector.xpath的快捷方式
    - 同理response.selector.css
    - selector.extract:把节点的内容用unicode形式返回
    - selector.re:允许用户通过正则选取内容
    
- 最主要的功能就是,更有效的写出xpath语句来