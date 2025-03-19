import turtle as t
'''
MIT开源许可证（要求在新的软件中包含此许可证）
The MIT License (MIT)

Copyright © 2025 StevenLin Studio

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
'''
'''
this file is made by Steven Lin Studio
用前须知：本文件如果要使用turtle画图，请提前加载turtlez库！
github开源地址：https://github.com/small-lin-jam/tools.py/
intx：带容错机制的int
floatx：带容错机制的float
strx：带容错机制的str
boolx：带容错机制的bool
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
'''
def intx(n):
    try:
        n=int(n)
    except ValueError as ve:
        print('这个数不能被格式化为整数，原因：', ve)
        n=input('请重新输入：')
        n=int(n)
    return n
def floatx(n):
    try:
        n=float(n)
    except ValueError as ve:
        print('这个数不能被格式化为浮点数，原因：', ve)
        n=input('请重新输入：')
        n=int(n)
    return n
def strx(n):
    n=str(n)
    return n
def boolx(n):
    n=bool(n)
    return n
def dcircle(cx=0,cy=0,lenth=200,h=360,fc='black'):
    print('正在检查cx：')
    floatx(cx)
    print('正在检查cy：')
    floatx(cy)
    print('正在检查lenth：')
    floatx(lenth)
    print('正在检查h：')
    floatx(h)
    print('正在检查fc：')
    strx(fc)
    print('检查完成，正在画图')
    t.pu()
    t.goto(cx,cy)
    t.seth(-90)
    t.fd(lenth)
    t.pd()
    t.seth(0)
    t.begin_fill()
    t.fillcolor(fc)
    t.circle(lenth,extent=h)
    t.end_fill()
def dmt(x=0,y=0,l1=200,l2=100,h=0,fc='black'):
    print('正在检查x：')
    floatx(x)
    print('正在检查y：')
    floatx(y)
    print('正在检查l1：')
    floatx(l1)
    print('正在检查l2：')
    floatx(l2)
    print('正在检查h：')
    floatx(h)
    print('正在检查fc：')
    strx(fc)
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
    floatx(x)
    print('正在检查y：')
    floatx(y)
    print('正在检查l：')
    floatx(l)
    print('正在检查h：')
    floatx(h)
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
    floatx(x)
    print('正在检查y：')
    floatx(y)
    print('正在检查l：')
    floatx(l)
    print('正在检查h：')
    floatx(h)
    print('正在检查fc：')
    strx(fc)
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