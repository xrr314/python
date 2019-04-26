import requests
import json
import time
import mysqlUtil
'''
提交答案
POST /yiban-web/stu/changeSituation.jhtml?_=1556268878977 HTTP/1.1
Host: 192.168.1.55:8080
Accept: application/json
Connection: keep-alive
X-Requested-With: XMLHttpRequest
Accept-Encoding: gzip, deflate
Accept-Language: zh-cn
Content-Type: application/x-www-form-urlencoded
Origin: http://192.168.1.55:8080
Content-Length: 69
Connection: keep-alive
User-Agent: Mozilla/5.0 (iPhone; CPU iPhone OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 yiban_iOS
Referer: http://192.168.1.55:8080/yiban-web/stu/toSubject.jhtml?courseId=2
Cookie: JSESSIONID=190D7A49CCCE7FF45E068E05E8EC9D18

获取题目
POST /yiban-web/stu/nextSubject.jhtml?_=1556268883548 HTTP/1.1
Host: 192.168.1.55:8080
Accept: application/json
Connection: keep-alive
X-Requested-With: XMLHttpRequest
Accept-Encoding: gzip, deflate
Accept-Language: zh-cn
Content-Type: application/x-www-form-urlencoded
Origin: http://192.168.1.55:8080
Content-Length: 10
Connection: keep-alive
User-Agent: Mozilla/5.0 (iPhone; CPU iPhone OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 yiban_iOS
Referer: http://192.168.1.55:8080/yiban-web/stu/toSubject.jhtml?courseId=2
Cookie: JSESSIONID=190D7A49CCCE7FF45E068E05E8EC9D18

'''
url="http://192.168.1.55:8080/yiban-web/stu/nextSubject.jhtml"
kw={
    '_':str(int(time.time()*1000)),
    'courseId':'2'
}
headers={
    'Accept': 'application/json',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-cn',
    'X-Requested-With': 'XMLHttpRequest',
    'Cookie': 'JSESSIONID=190D7A49CCCE7FF45E068E05E8EC9D18',
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 yiban_iOS',
    'Referer': 'http://192.168.1.55:8080/yiban-web/stu/toSubject.jhtml?courseId=2',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Content-Length': '10',
    'Connection': 'keep-alive'
}
'''
    获取题目
'''
def nextSubect():
    rsp=requests.post(url,params=kw,headers=headers)
    data = dict()
    dictinfo = json.loads(rsp.text)
    print(dictinfo)
    uuid = dictinfo['data']['uuid']
    data.update({'uuid':uuid})
    # print(uuid)
    subject = dictinfo['data']['nextSubject']
    # print(subject)
    score = subject['score']
    type = subject['subType']
    subDescript = subject['subDescript']
    optionCount = subject['optionCount']
    data.update({'score':score})
    data.update({'type': type})
    data.update({'subDescript': subDescript})
    data.update({'optionCount': optionCount})
    print('score:'+str(score),'subDescript:'+subDescript,'optionCount:'+str(optionCount))
    for i in range(0,6):
        if i < int(optionCount):
            # print('option' + str(i), subject['option' + str(i)])
            data.update({'option' + str(i):subject['option' + str(i)]})
        else:
            data.update({'option' + str(i):None})
    return  data
'''
    题目添加
'''
def addExam(data):
    result = mysqlUtil.queryById(data['uuid'])
    if(not result):
        str = mysqlUtil.insert(data)
        return str
    return result
'''
    获取题目答案
'''
def getPass(tuple):
    '''
    如果原则的最后一个元素不为空,则说明已经存在了正确答案,直接获取
    如果不存在,则返回第一选择,从请求中获取答案,并保存
    :param tuple:
    :return:
    '''
    if not tuple(-1) is None:
        pwd = tuple(-1)
    else:
        pass

if __name__ == '__main__':
    i = 0
    while(1):
        i = i+1
        print('==========================开始第'+str(i)+'题=========================')
        data = nextSubect()
        result = addExam(data)
        if isinstance(result, tuple):
            getPass(tuple)
        else:
            print(result)
        time.sleep(5)