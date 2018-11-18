# 验证码问题
- 验证码:防止机器人和爬虫
- 分类:
    - 简单图片
    - 极验(www.geetes.com)
    - 12306
    - 电话验证
    - Google验证
    
- 验证码破解
    - 通用方法:
        - 下载网页和验证码
        - 手动输入验证号码
    - 简单图片
        - 使用图像识别软件或者文字识别软件
        - 可以使用第三方图像验证码破解网站,www.chaojiying.com
    - 极验(www.geetes.com)
        - 破解比较麻烦
        - 可以模拟鼠标等移动
        - 一直在进化
    - 12306
        - 手动识别
    - 电话验证
        - 语音识别
    - Google验证
    
# Tesseract
- 机器视觉领域的基础软件
- OCR:OpticalCharcterRecognition,光学文字识别
- Tessert: 一个ocr库,Google赞助
- 安装:
    - windows: https://jingyan.baidu.com/article/219f4bf788addfde442d38fe.html
    - mac: brew install tesseract
    - linux: apt-get install tesseract-ocr
        aptitude install tesseract-ocr
    - 安装完成需要设置环境变量
        - win: https://www.cnblogs.com/jianqingwang/p/6978724.html
- 安装完后还需要pytesseract
    - pip install pytesseract
- 控制态简单测试下
    source activate 环境名称
        如果忘记了可以使用conda env list查询所有的运行环境名称
    进入到图片所在文件夹下
    tesseract 图片名 识别后文件名