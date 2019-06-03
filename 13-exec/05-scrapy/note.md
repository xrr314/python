# scrapy框架学习
    - 框架
    - 爬虫变得相当简单
    - 异步网络框架(Twisted)自带多线程
    - 提供各种接口以及中间件管理
    
## scrapy长什么样子
    - Spider (爬虫)
        - 1.初次发起爬虫请求
        - 2.解析response得到的数据,
            若是url地址将url地址传递给调度器尽心循环爬取
            若是数据传递给item pipline
    - Scheduler(调度器)
        - 负责接受引擎发送过来的request请求,在此处进行队列整合
    - downloader(下载器)
        - 主要负责从互联网进行网页内容的请求
    - Item Pipline(数据存储)
        - 主要负责spider中得到数据(item),进行数据的处理与保存
    - Scrapy Engine(引擎)
        - 负责spider,Item pipline,scheduler,download之间的协调与通信/数据的传送
    - Download Middlewares
        - 下载中间件,主要进行下载功能的扩展
    - Spider Middlewares
        - 主要负责扩展spider功能/扩展与引擎之间的通信功能
        
# scrapy框架的安装
    - 搭建虚拟环境
        - 查看conda env list
    - 创建虚拟环境
        - conda create -n spider_env python=3.6
    - 创建完成激活虚拟环境
        - liunx : source activate spider_env
        - win: activate spider_env
    - 安装scrapy框架
        pip install scrapy
    - 查看环境中已安装的内容    
        pip list
        
    - 环境搭建问题
        - 不推荐在win下使用,存在大量其他依赖软件
            c++ 14.0
        - 非conda环境需要安装pywin32,twisted,wheel
        
# 创建第一个scrapy项目
    # 创建项目
        - scrapy startproject [项目名称]
    # 创建爬虫实例
        - scrapy genspider [SpiderName] [domain.com]
    # 注意: 爬虫名称不要和项目名称相同
        scrapy默认遵循robots协议
            http://www.baidu.com/robots.txt
    