'''
爬取福建省司法厅律师详情
http://120.35.30.141/was5/web/search?channelid=272193&sortfield=-pzrq&prepage=10&page=1
http://120.35.30.141/was5/web/search?channelid=272193&sortfield=-pzrq&prepage=10&page=2

通过页面访问得到
http://120.35.30.141/was5/web/search?channelid=272193&sortfield=-pzrq&prepage=1000&page=1
可以返回全部的信息
'''
import requests
import json
import xlsxwriter
import pandas as pd

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36',
    'Referer':'http://120.35.30.141/wsbs/bmfwcx/lsgl/lssws/?swsmc=&swsdz=&fzr=',
    'Host':'120.35.30.141'
}
url = 'http://120.35.30.141/was5/web/search?channelid=272193&sortfield=-pzrq&prepage=1000&page=1'
rsp = requests.get(url,headers=headers)
# print(type(rsp.text),rsp.text)
data = rsp.text.replace("\\","/")
# print(data)
json_data = json.loads(data)
# print(json_data)
data = json_data['docs']
print(type(data),data)

recid = []
swsmc = []
fzr = []
zzxs =[]
zyxkzh = []
pzrq = []
zwjc = []
ywqc = []
swsdz = []
zgjg = []
pzwh =[]
slzc = []
zsfs = []
scfzrq = []
lxdh = []
wz = []
swdjh = []
hhr = []
yzbm = []
zzls = []
jzls = []
cz = []
sfzx = []
sqs = []
xsq = []
oldid = []
ndkhqk = []
jlqk = []
bgqk = []
cfqk = []

for d in data:
    if 'recid' in d.keys():
        recid.append(d['recid'])
    else:
        recid.append('')

    if 'swsmc' in d.keys():
        swsmc.append(d['swsmc'])
    else:
        swsmc.append('')

    if 'fzr' in d.keys():
        fzr.append(d['fzr'])
    else:
        fzr.append('')

    if 'zzxs' in d.keys():
        zzxs.append(d['zzxs'])
    else:
        zzxs.append('')

    if 'zyxkzh' in d.keys():
        zyxkzh.append(d['zyxkzh'])
    else:
        zyxkzh.append('')

    if 'pzrq' in d.keys():
        pzrq.append(d['pzrq'])
    else:
        pzrq.append('')

    if 'zwjc' in d.keys():
        zwjc.append(d['zwjc'])
    else:
        zwjc.append('')

    if 'ywqc' in d.keys():
        ywqc.append(d['ywqc'])
    else:
        ywqc.append('')

    if 'swsdz' in d.keys():
        swsdz.append(d['swsdz'])
    else:
        swsdz.append('')

    if 'zgjg' in d.keys():
        zgjg.append(d['zgjg'])
    else:
        zgjg.append('')

    if 'pzwh' in d.keys():
        pzwh.append(d['pzwh'])
    else:
        pzwh.append('')

    if 'slzc' in d.keys():
        slzc.append(d['slzc'])
    else:
        slzc.append('')

    if 'zsfs' in d.keys():
        zsfs.append(d['zsfs'])
    else:
        zsfs.append('')

    if 'scfzrq' in d.keys():
        scfzrq.append(d['scfzrq'])
    else:
        scfzrq.append('')

    if 'lxdh' in d.keys():
        lxdh.append(d['lxdh'])
    else:
        lxdh.append('')

    if 'wz' in d.keys():
        wz.append(d['wz'])
    else:
        wz.append('')

    if 'swdjh' in d.keys():
        swdjh.append(d['swdjh'])
    else:
        swdjh.append('')

    if 'hhr' in d.keys():
        hhr.append(d['hhr'])
    else:
        hhr.append('')

    if 'yzbm' in d.keys():
        yzbm.append(d['yzbm'])
    else:
        yzbm.append('')

    if 'zzls' in d.keys():
        zzls.append(d['zzls'])
    else:
        zzls.append('')

    if 'jzls' in d.keys():
        jzls.append(d['jzls'])
    else:
        jzls.append('')

    if 'cz' in d.keys():
        cz.append(d['cz'])
    else:
        cz.append('')

    if 'sfzx' in d.keys():
        sfzx.append(d['sfzx'])
    else:
        sfzx.append('')

    if 'sqs' in d.keys():
        sqs.append(d['sqs'])
    else:
        sqs.append('')

    if 'xsq' in d.keys():
        xsq.append(d['xsq'])
    else:
        xsq.append('')

    if 'oldid' in d.keys():
        oldid.append(d['oldid'])
    else:
        oldid.append('')

    if 'ndkhqk' in d.keys():
        ndkhqk.append(d['ndkhqk'])
    else:
        ndkhqk.append('')

    if 'jlqk' in d.keys():
        jlqk.append(d['jlqk'])
    else:
        jlqk.append('')

    if 'bgqk' in d.keys():
        bgqk.append(d['bgqk'])
    else:
        bgqk.append('')

    if 'cfqk' in d.keys():
        cfqk.append(d['cfqk'])
    else:
        cfqk.append('')

df = pd.DataFrame({
'recid':recid,
'swsmc':swsmc,
'fzr':fzr,
'zzxs':zzxs,
'zyxkzh':zyxkzh,
'pzrq':pzrq,
'zwjc':zwjc,
'ywqc':ywqc,
'swsdz':swsdz,
'zgjg':zgjg,
'pzwh':pzwh,
'slzc':slzc,
'zsfs':zsfs,
'scfzrq':scfzrq,
'lxdh':lxdh,
'wz':wz,
'swdjh':swdjh,
'hhr':hhr,
'yzbm':yzbm,
'zzls':zzls,
'jzls':jzls,
'cz':cz,
'sfzx':sfzx,
'sqs':sqs,
'xsq':xsq,
'oldid':oldid,
'ndkhqk':ndkhqk,
'jlqk':jlqk,
'bgqk':bgqk,
'cfqk':cfqk
})

workbook=xlsxwriter.Workbook('v00_xls_lvshi.xlsx')
worksheet = workbook.add_worksheet()
format_columname=workbook.add_format({'bold':True,'font_color':'blue','bg_color':'purple'})
format=workbook.add_format({'font_name':'Times New Roman'})

for col in range(len(df.columns)):
    worksheet.write(0,col,df.columns[col],format_columname)
    # print(df.columns[col])
    # print(df.iloc[:,col])
    for row in range(len(df.iloc[:,col])):
        worksheet.write(row + 1, col,df.iloc[:,col].values[row])

# print(type(df.iloc[:,1].values),df.iloc[:,1].values[0])
# for col in df.iloc[:,2]:


workbook.close()