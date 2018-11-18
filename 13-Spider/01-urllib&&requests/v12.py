from  urllib import request,error

if __name__ == '__main__':
    url='http://www.renren.com/968526175/profile'
    headers={'cookie':'anonymid=jnvqxgzn5djm9t; depovince=GW; _r01_=1; ick_login=bc1c8f3c-21a7-4750-8663-d12851e34c80; ick=bb2cfdad-4db4-452c-aae1-d09078403fa6; t=f6840c57bc61ce7dea86b3bd7ee719e25; societyguester=f6840c57bc61ce7dea86b3bd7ee719e25; id=968526175; xnsid=3ae98dd7; XNESSESSIONID=2afcd4448340; WebOnLineNotice_968526175=1; JSESSIONID=abc7kVeqWFFQ9c9j3ffBw; jebecookies=a30cca4c-4d1a-4502-bcb2-87e8c3554609|||||; jebe_key=ba26e9cd-d214-4f58-ae9a-bf0d4e18713f%7C0de978deb2b2dcd7eabb56d3f9e1e564%7C1540904982322%7C1%7C1540905053294; wp_fold=0'}

    req = request.Request(url,headers=headers)
    rsp = request.urlopen(req)
    html = rsp.read().decode()

    with open('rsp.html','w')as f:
        f.write(html)