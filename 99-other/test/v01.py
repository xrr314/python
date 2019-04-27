import requests
import json
import time
import mysqlUtil

url="http://192.168.88.101:8080/yiban-web/stu/nextSubject.jhtml"
kw={
    '_':str(int(time.time()*1000)),
    'courseId':'2'
}
curdict = {'0': 'A','1':'B','2':'C','3':'D','4':'E','5':'F'}
backcurdict = {'A':'0','B':'1','C':'2','D':'3','E':'4','F':'5'}

headers={
    'Host': '192.168.88.101:8080',
    'Accept': 'application/json',
    'Connection': 'keep-alive',
    'X-Requested-With': 'XMLHttpRequest',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-cn',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Origin': 'http://192.168.88.101:8080',
    'Content-Length': '10',
    'Connection': 'keep-alive',
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 yiban_iOS',
    'Referer': 'http://192.168.88.101:8080/yiban-web/stu/toSubject.jhtml?courseId=2',
    'Cookie': 'JSESSIONID=A9B294AFF104E32339143CCD159239D9',

}

backHeaders = {
    'Accept': 'application/json',
    'Connection': 'keep-alive',
    'X-Requested-With': 'XMLHttpRequest',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-cn',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Origin': 'http://192.168.88.101:8080',
    'Content-Length': '69',
    'Connection': 'keep-alive',
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 yiban_iOS',
    'Referer': 'http://192.168.88.101:8080/yiban-web/stu/toSubject.jhtml?courseId=2',
    'Cookie': 'JSESSIONID=A9B294AFF104E32339143CCD159239D9'
}


'''
    获取题目
'''
def nextSubect():
    rsp=requests.post(url,params=kw,headers=headers)
    data = dict()
    print(rsp)
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
    '''
    判断题目是否保存在了数据库中,没有的话添加
    :param data:
    :return:
    '''
    result = mysqlUtil.queryById(data['uuid'])
    if(not result):
        print('题目不存在开始添加')
        str = mysqlUtil.insert(data)
        return str
    print('题目存在返回,查询结果')
    return result
'''
    获取题目答案
'''
def getPass(tuple,data):
    '''
    如果原则的最后一个元素不为空,则说明已经存在了正确答案,直接获取
    如果不存在,则返回第一选择,从请求中获取答案,并保存
    :param tuple:
    :return:
    '''
    if not tuple(-1) is None:
        pwd = tuple(-1)
        cur = ''
        for i in range(int(data['optionCount'])):
            if(pwd == data['option'+str(i)]):
                cur = curdict[str(i)]
        if(cur == ''):
            print('=====题库中午答案返回答案A====')
            return 'A'
        print('=====题库中保存答案为'+cur)
        return cur
    else:
        return False

def back(answer,data):
    '''
    答题
    :return:
    '''
    uuid = data['uuid']
    backkw = {
        '_':str(int(time.time()*1000)),
        'courseId': '2',
        'answer':answer,
        'uuid':uuid
    }
    rsp = requests.post('http://192.168.88.101:8080/yiban-web/stu/changeSituation.jhtml', params=backkw, headers=backHeaders)
    backdict = json.loads(rsp.text)
    print(backdict)
    '''
        如果获取正确答案,并返回
    '''
    if(backdict['data']['rightAnswer']==True):
        return data['option'+backcurdict[answer]]
    else:
        print(backdict['data'])
        curAns = backdict['data']['rightOption'].split('.')[-1]
        return curAns

def updateCur(uuid,cur):
    '''
    修正数据库内的正确答案
    :param uuid:
    :param cur:
    :return:
    '''
    mysqlUtil.updatecur(uuid,cur)

if __name__ == '__main__':
    # print(nextSubect())
    i = 0
    while(1):
        i = i+1
        print('==========================开始第'+str(i)+'题=========================')
        data = nextSubect()
        result = addExam(data)
        '''查询题目存在'''
        uuid = data['uuid']
        print('uuid:'+uuid)
        if isinstance(result, tuple):
            print('===题目存在====')
            '''获取答案,如果已经保存过答案,没有的话,就直接返回选项A'''
            cur = getPass(tuple,data)
            '''将答案返回给系统,判断答案是否正确'''
            curAns = back(cur,data)
            '''将正确答案保存到数据库中'''
            if isinstance(curAns,str):
                print(curAns)
                updateCur(uuid,curAns)
        elif isinstance(result, str):
            print('====添加题目不存在====')
            '''题目不存在直接返回A,从系统获取争取答案'''
            curAns = back('A', data)
            '''修改数据库中题目答案'''
            updateCur(uuid, curAns)
