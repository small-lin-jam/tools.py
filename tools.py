import math,turtle as t
'''
开源许可证法律说明:
当任何人删除MIT开源许可证时，原作者有权按照违约进行处理，我们不允许任何诋毁原作者的情况发生，也不希望这些代码被恶意改造，请注意辨别

开源说明：
如果您在别的平台上发现了有人在贩卖本文件，请不要购买。如果想要合作，请联系github上关于tools.py的论坛，我们不会给予钱财，但会在下方留下您的名字
我们鼓励他人去合法修改本文件，但如果被恶意使用，我们将考虑停止对商业（包括但不限于零售）的支持

MIT开源许可证（要求在新的软件中包含此许可证）
The MIT License (MIT)

Copyright © 2025 StevenLin Studio

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
'''
'''
原作者说明：
this file is made by Steven Lin Studio
请注意：我们不允许有删除开源许可证的行为发生，一经发现，按违约处理

开发人员名单：
Steven Lin Studio管理与发布人员（林先生）

用前须知：本文件如果要使用turtle画图，请提前加载turtle库！
github开源地址：https://github.com/small-lin-jam/tools.py/
inputx：带容错机制的高级input
    string：在'请输入'后面的变量名（仅影响用户体验）
    n：指定格式化模式
        str、string、1、strx：格式化为字符串
        int、2、intx：格式化为整数
        float、3、floatx：格式化为浮点数
        bool、4、boolx：格式化为布尔值（True或False）
intx：带容错机制的int
floatx：带容错机制的float
strx：带容错机制的str
boolx：带容错机制的bool
sumx：带容错机制的加
    n1：加数1
    n2：加数2
subx：带容错机制的减
    n1：被减数
    n2：减数
mulx：带容错机制的乘
    n1：乘数1
    n2：乘数2
divx：带容错机制的除
    n1：被除数
    n2：除数
powerx：带容错机制的乘方
    nb：底数
    ne：指数
rootx：带容错机制的开根号
    rad：被开根数
    index：根号中的次数
divzx：带容错机制的除（仅保留整数）
    n1：被除数
    n2：除数
divxx：带容错机制的除（仅保留小数）
    n1：被除数
    n2：除数
dsyah：计算等腰三角形三个角
    l1：等腰三角形底边
    l2：等腰三角形的腰
dsnah：计算三角形三个角
    l1：三角形底边
    l2：三角形的左腰
    l3：三角形的右腰
dcircle：根据所给圆心画圆
    cx：确定圆心x坐标
    cy：确定圆心y坐标
    length：确定圆半径（r）
    h：圆弧度数（正负均可，正：顺时针画圆，负：逆时针画圆）
    fc：填充颜色（如果不要填充，请输入被覆盖部分的颜色）
    警告：开始位置为圆心正下方length长度
dmt：根据所给长方形左上角顶点画长方形
    x：确定顶点x坐标
    y：确定顶点y坐标
    l1：确定长方形的长
    l2：确定长方形的宽
    h：面向方向（正右为0）
    fc：填充颜色（如果不要填充，请输入被覆盖部分的颜色）
dl:根据所给线中点画直线
    x：确定中点x坐标
    y：确定中点y坐标
    l：直线长度
    h：确定从直线中点到直线开始点（默认在正下方）的方位（默认-90）
ds:根据所给三角形左下角顶点画等边三角形
    x：确定三角形左下角顶点x坐标
    y：确定三角形左下角顶点y坐标
    l：确定边长（不是三条边的总和）
    h：确定底边方向（默认为正右，数据为0）
    fc：填充颜色（如果不要填充，请输入被覆盖部分的颜色）
dsy:根据所给三角形左下角顶点画等腰三角形
    x：确定三角形底边中点x坐标
    y：确定三角形底边中点y坐标
    l1：确定底边长
    l2：确定腰长（不是两腰总和）
    h：确定底边方向（默认为正右，数据为0）
    fc：填充颜色（如果不要填充，请输入被覆盖部分的颜色）
dsn:根据所给三角形左下角顶点画三角形
    x：确定三角形左下角顶点x坐标
    y：确定三角形左下角顶点y坐标
    l1：确定底边长
    l2：确定左腰长
    l3：确定右腰长
    h：确定底边方向（默认为正右，数据为0）
    fc：填充颜色（如果不要填充，请输入被覆盖部分的颜色）
'''
#输入/输出处理
def inputx(string='数据',n='str'):
    strx(n)
    strx(string)
    string=format('请输入'+string+':')
    a=input(string)
    if n=='str' or n=='string' or n=='1' or n=='strx':
        a=strx(a)
    elif n=='int' or n=='2' or n=='intx':
        a=intx(a)
    elif n=='float' or n=='3' or n=='floatx':
        a=floatx(a)
    elif n=='bool' or n=='4' or n=='boolx':
        a=boolx(a)
    else:
        a=strx(a)
    return a
#基础数学运算
def intx(n):
    try:
        n=int(n)
    except ValueError as err:
        print('这个数不能被格式化为整数，原因：', err)
        n=input('请重新输入：')
        n=intx(n)
    except TypeError as err:
        print('这个数不能被格式化为整数，原因：', err)
        n=input('请重新输入：')
        n=intx(n)
    return n
def floatx(n):
    try:
        n=float(n)
    except ValueError as err:
        print('这个数不能被格式化为浮点数，原因：', err)
        n=input('请重新输入：')
        n=floatx(n)
    except TypeError as err:
        print('这个数不能被格式化为浮点数，原因：', err)
        n=input('请重新输入：')
        n=floatx(n)
    return n
def strx(n):
    n=str(n)
    return n
def boolx(n):
    n=bool(n)
    return n
def sumx(n1,n2):
    floatx(n1)
    floatx(n2)
    n=n1+n2
    return n
def subx(n1,n2):
    floatx(n1)
    floatx(n2)
    n=n1-n2
    return n
def mulx(n1,n2):
    floatx(n1)
    floatx(n2)
    n=n1*n2
    return n
def divx(n1,n2):
    floatx(n1)
    floatx(n2)
    n=n1/n2
    return n
def powerx(nb,ne):
    floatx(nb)
    floatx(ne)
    n=nb**ne
    return n
def rootx(rad,index):
    floatx(rad)
    floatx(index)
    try:
        n=complex(rad)**(1/index)
    except ValueError as ve:
        print('这个数不能被开根号，原因：', ve)
        rad=input('请重新输入被开根数：')
        index=input('请重新输入根号中的次数：')
        n=rootx(rad,index)
    return n
#高阶计算
def divzx(n1,n2):
    floatx(n1)
    floatx(n2)
    n=n1//n2
    return n
def divxx(n1,n2):
    floatx(n1)
    floatx(n2)
    n=n1%n2
    return n
def dsyah(l1,l2):
    if l1<=0 or l2<=0: return None  
    angle=math.degrees(math.acos((2*l2**2-l1**2)/(2*l2**2)))
    return angle
def dsnah(l1,l2,l3):
    l1,l2,l3=floatx(l1),floatx(l2),floatx(l3)
    if l1 <=0 or l2<=0 or l3<=0: return None
    if l1+l2<=l3 or l1+l3<=l2 or l2+l3<=l1:
        return None,None,None
    angle_A=math.degrees(math.acos((l2**2+l3**2-l1**2)/(2*l2*l3)))
    angle_B=math.degrees(math.acos((l1**2+l3**2-l2**2)/(2*l1*l3)))
    angle_C=180-angle_A-angle_B
    return angle_A,angle_B,angle_C
#turtle画图（需要在外部重新import turtle）
def dmt(x=0,y=0,l1=200,l2=100,h=0,fc='black'):
    print('正在检查x：')
    x=floatx(x)
    print('正在检查y：')
    y=floatx(y)
    print('正在检查l1：')
    l1=floatx(l1)
    print('正在检查l2：')
    l2=floatx(l2)
    print('正在检查h：')
    h=floatx(h)
    print('正在检查fc：')
    fc=strx(fc)
    print('检查完成，正在画图')
    t.pu()
    t.goto(x,y)
    t.seth(h)
    t.pd()
    t.begin_fill()
    t.fillcolor(fc)
    for _ in range(2):
        t.fd(l1)
        t.rt(90)
        t.fd(l2)
        t.rt(90)
    t.end_fill()
def dl(x=0,y=0,l=100,h=-90):
    print('正在检查x：')
    x=floatx(x)
    print('正在检查y：')
    y=floatx(y)
    print('正在检查l：')
    l=floatx(l)
    print('正在检查h：')
    h=floatx(h)
    print('检查完成，正在画图')
    t.pu()
    t.goto(x,y)
    t.seth(h)
    l1=l/2
    t.fd(l1)
    t.pd()
    t.rt(180)
    t.fd(l)
def ds(x=0,y=0,l=100,h=0,fc='black'):
    print('正在检查x：')
    x=floatx(x)
    print('正在检查y：')
    y=floatx(y)
    print('正在检查l：')
    l=floatx(l)
    print('正在检查h：')
    h=floatx(h)
    print('正在检查fc：')
    fc=strx(fc)
    print('检查完成，正在画图')
    t.pu()
    t.goto(x,y)
    t.seth(h)
    l1=l/2
    t.fd(l1)
    t.pd()
    t.begin_fill()
    t.fillcolor(fc)
    for _ in range(3):
        t.lt(120)
        t.fd(l)
    t.end_fill() 
def dsy(x=0,y=0,l1=100,l2=100,h=0,fc='black'):
    print('正在检查x：')
    x=floatx(x)
    print('正在检查y：')
    y=floatx(y)
    print('正在检查l1：')
    l1=floatx(l1)
    print('正在检查l2：')
    l2=floatx(l2)
    print('正在检查h：')
    h=floatx(h)
    print('正在检查fc：')
    fc=strx(fc)
    print('检查完成，正在画图')
    angle = dsyah(l1, l2)
    if angle is None:
        print("错误：边长需大于0")
        return
    t.pu()
    t.goto(x,y)
    t.seth(h) 
    t.pd()
    t.begin_fill()
    t.fillcolor(fc)
    t.fd(l1)
    t.left(180-angle)
    t.fd(l2)
    t.goto(x,y)
    t.end_fill()
    t.setheading(h)
def dsn(x=0,y=0,l1=100,l2=100,l3=100,h=0,fc='black'):
    print('正在检查x：')
    x=floatx(x)
    print('正在检查y：')
    y=floatx(y)
    print('正在检查l1：')
    l1=floatx(l1)
    print('正在检查l2：')
    l2=floatx(l2)
    print('正在检查l3：')
    l3=floatx(l3)
    print('正在检查h：')
    h=floatx(h)
    print('正在检查fc：')
    fc=strx(fc)
    print('检查完成，正在画图')
    angle_A,angle_B,angle_C=dsnah(l1,l2,l3)
    t.pu()
    t.goto(x,y)
    t.seth(h)
    t.pd()
    t.begin_fill()
    t.fillcolor(fc)
    t.fd(l1)
    t.left(180-angle_B)
    t.fd(l2)
    t.left(180-angle_C)
    t.fd(l3)
    t.left(180-angle_A)
    t.end_fill()