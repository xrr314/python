from urllib import request,error

if __name__ == '__main__':
    url='http://www.renren.com/968526175/profile'

    rsp=request.urlopen(url)
    html=rsp.read().decode()

    with open('rsp.html','w')as f:
        f.write(html)

    #print(html)