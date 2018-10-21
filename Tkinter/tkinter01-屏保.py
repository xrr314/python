import random
import tkinter


class RandomBall():
    '''
        定义运动的球的类
    '''

    def __init__(self, canvas, scrnwidth, scrnheight):
        '''
            canvas画布.所有内有都应该在画布上显示出来,此处通过此变量传入
            scrnwidth/scrnheight屏幕宽高
        '''
        self.canvas=canvas
        # 定义球出现的初始位置,尽量不要让球在边框出现
        self.xpos = random.randint(60, int(scrnwidth) - 60)
        self.ypos = random.randint(60, int(scrnheight) - 60)

        # 定义球运动的速度
        # 模拟运动,不断的擦掉原来的画,然后在一个新的地方在出现新的绘制
        # 定义球体每次的偏移量的范围
        self.xvelocity = random.randint(4, 20)
        self.yvelocity = random.randint(4, 20)

        # 屏幕的大小
        self.scrnwidth = scrnwidth
        self.scrnheight = scrnheight

        # 定义球出现的大小(定义球的半径)
        self.radius = random.randint(10, 60)

        # 定义颜色
        # RGB定义:三个数字,每一个数字的值0-255,表示红绿蓝的三个颜色
        # 某些系统可以直接用英文
        # 此处用lambda表达式
        c = lambda: random.randint(0, 255)
        self.color = '#%02x%02x%02x' % (c(), c(), c())

    def create_ball(self):
        '''
            用构造函数定义的变量值,在画板上画一个球
        '''
        # tkinter没有画圆形的函数,只有一个椭圆的函数,画椭圆需要定义2个坐标
        # 在长方形内画椭圆,我们需要定义长方形左上角和右下角就好,系统会自动生成长方形内切椭圆
        # 求两个坐标的方法,已知圆形和半径
        # 左上角
        x1 = self.xpos - self.radius
        y1 = self.ypos - self.radius
        # 右下角
        x2 = self.xpos + self.radius
        y2 = self.ypos + self.radius

        # 画圆
        # fill表示填充的颜色
        # outlines边框的颜色
        self.item = self.canvas.create_oval(x1, y1, x2, y2, fill=self.color, outline=self.color)

    def move_ball(self):
        # 移动球的移动方向,需要控制球的方向
        # 每次移动后求都有一个新的坐标
        self.xpos += self.xvelocity
        self.ypos += self.yvelocity

        # 之后我们需要判断是否会撞墙
        # 撞右边
        if (self.xpos + self.radius) >= self.scrnwidth:
            self.xvelocity *= (-1)
        # 撞左边
        if (self.xpos - self.radius) <= 0:
            self.xvelocity *= (-1)

        # 撞下边
        if (self.ypos + self.radius) >= self.scrnheight:
            self.yvelocity *= (-1)
        # 撞上面
        if (self.ypos - self.radius) <= 0:
            self.yvelocity *= (-1)

            # 在画布上挪动图画
        self.canvas.move(self.item, self.xvelocity, self.yvelocity)


class ScreenSaver():
    '''
        定义屏保的类
        可以被启动
    '''
    # 如何装随机产生的球?
    balls = list()

    def __init__(self):
        # 定义球随机个数
        self.num_balls = random.randint(5, 10)
        #
        self.root = tkinter.Tk()
        # 取消边框
        self.root.overrideredirect(1)

        # 任何鼠标移动都需要取消
        self.root.bind('<Motion>', self.myquit)

        # 得到屏幕大小
        w, h = self.root.winfo_screenwidth(), self.root.winfo_screenheight()
        # 创建画布,包括画布的归属,规格
        self.canvas = tkinter.Canvas(self.root, width=w, height=h)
        self.canvas.pack()

        # 在画布上画球
        for i in range(self.num_balls):
            ball = RandomBall(canvas=self.canvas, scrnwidth=w, scrnheight=h)
            ball.create_ball()
            self.balls.append(ball)

        self.run_screen_saver()
        self.root.mainloop()

    def run_screen_saver(self):
        for ball in self.balls:
            ball.move_ball()
        # after是200ms之后启动一个函数,第二个参数是启动的函数
        self.canvas.after(30, self.run_screen_saver)

    def myquit(self, e):
        # 此处只是利用了时间处理机制
        # 实际上并不关心时间的类型
        self.root.destroy()


if __name__ == "__main__":
    ScreenSaver()