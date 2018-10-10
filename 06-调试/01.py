def SayHello(name):
    print('I want to say hello with your,{0}'.format(name))
    print('Hello,{0}'.format(name))
    print('Done...............')

if __name__ == '__main__':
    print('* '*20)
    name=input('Please input your name:')
    SayHello(name)
    print('@@'*20)