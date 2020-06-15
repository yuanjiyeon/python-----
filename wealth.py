import math  # 用来取整个
import xlrd  # 用来导入表格
import numpy as np  # 绘图
import matplotlib as mpl  # 绘图
import matplotlib.pyplot as plt  # 绘图
import tkinter as tk
import tkinter.font as tf
import os
# 特殊情况的加减仓
def addmoney( addday, addmon,lost1):
    global y, total,lost
    if i - j + 1 == addday :
        y += addmon
        total += addmon
        lost=lost1 #修正现在有的收益率
#标题改名用
def changename(name):
    if name=='yf':
       return '易方达'
    elif name=='bj':
        return '百家'
    elif name=='ccyl':
        return '中欧医疗'
    else:
        return  '易方达消费'
def buttonValue():
   global x1
   x1='bj'
def buttonValue1():
   global x1
   x1='yf'
def buttonValue11():
   global x1
   x1='gfxf'
def buttonValue12():
    global x1
    x1 = 'ccyl'
def buttonValue0():
   global mrow
   mrow=0
   root.destroy()
def buttonValue01():
   global mrow
   mrow=1
   root.destroy()
baijia = 'bj'  # 百家优选
yifang = 'yf'  # 易方达
guangfaxiaofei = 'gfxf'  #易方达消费
changchengyiliao= 'ccyl' #中欧医疗
listJ=[baijia, yifang, guangfaxiaofei, changchengyiliao]
root=tk.Tk()
root.minsize(500,700)
f=tf.Font(family='叶根友毛笔行书2.0版',size=48)
b1=tk.Button(root,text = '百家',font=f,command=buttonValue,bg='BurlyWood')
b1.pack()
b2=tk.Button(root,text = '易方达',font=f,command=buttonValue1,bg='BurlyWood')
b2.pack( )
b2=tk.Button(root,text = '易方达消费',font=f,command=buttonValue11,bg='BurlyWood')
b2.pack( )
# b2=tk.Button(root,text = '中欧医疗',font=f,command=buttonValue12,bg='BurlyWood')
# b2.pack( )
b3=tk.Button(root,text = '测试数据',font=f,command=buttonValue0,bg='BurlyWood')
b3.pack()
b4=tk.Button(root,text = '实际数据',font=f,command=buttonValue01,bg='BurlyWood')
b4.pack()
root.mainloop()
# print(x1)
# x1 = input('请输入基金的全拼###bj#####yf######yfxf'+'\n')
#
# 用于区分基金进行减仓
#mrow = int(input('请输入要测试数据，0代表测试数据，1代表实际数值'))# 测试数据 0 是测试数据
url = xlrd.open_workbook(r'D:\Github\First\bin\test.xls')  # 打开表格
try:
    aa = url.sheet_by_name(x1)  # 读取其中内容
except:
    print('出错')
nrow = aa.nrows  # 行数
ncol = aa.ncols  # 列数
lilu = aa.col_values(mrow)  # 读取其中的某一列
touZi=aa.col_values(8)
# lilu = ["-0.0003", "-0.0075", "-0.0513", "0.0293", "-0.03","-0.0138","0.038","-0.0570",".0078","-0.0115","0.0032","0.0051","-0.059","0.0169","0.0403","0.0113","-0.0077","-0.0182","0.0049","-0.0052","0.0368","-.01","0.0211","-0.0051","0.004","-.0259","-.0098",".0354","0.0112",".0202","0.0068"]
doubleY = 199.7
doubleTotal = 200
y = doubleY  # 进场金额，，是扣过0.15%手续费用
i = 0  # 用来纪录天数
j = 0  # 用来统计周末天数
total = doubleTotal  # 计算总共投入金额
lostmoney = []  # 绘图y轴数据 ，显示损失的钱
day = []  # 绘图x轴数据，显示持仓的天数
allmoney = []  # 用来储存总金额
lost=0 #修正收益率
# 计算金额循环
while i < len(lilu):  # 读取所有的基金净值
    y = y * float(lilu[i]) + y  # 计算得利后的金额
    #print('亏损',total-y+lost)
    if lilu[i] !=0:
     lostmoney.append(y - total-lost)  # 存储
    if float(lilu[i]) < 0:  # 净值为负开始加仓，加仓规则每损失1%=100，净值为正持有不动
        x = float(lilu[i])
        y += -doubleY * math.ceil(x * 100)
        total += -doubleTotal * math.ceil(x * 100)
        if -math.ceil(x * 100) < 1:  # 不足1%，加仓100
            y += doubleY
            total += doubleTotal
    if lilu[i] == 0.0:  # 持有天数要去除周末
        j += 1
    print('现金',y,'总投入',total,'利率',lilu[i])
    i += 1
    if lilu[i-1] !=0:
        day.append(i - j)  # 存储
        allmoney.append(total)  # 存储
    if x1 == 'gfxf' and lilu[i-1]!=0:
        addmoney(2,-400,6)#错过的加仓
    if x1 == 'yf'and lilu[i-1]!=0:
        addmoney( 61, -200,5)
    if x1 == 'bj'and lilu[i-1]!=0:
        addmoney( 20, 200,0.11)
    if i != len(lilu):  # 读取表格中有空白内容
        if lilu[i] == "":
            break;
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
plt.figure(figsize=(30, 50))  # 窗口大小
#plt.plot(day, lostmoney, "b--", linewidth=.5, marker='o')  # 绘制折线图
l=round(lostmoney[len(lostmoney)-1],2)
label1='投资回报: '+str(l)#增加说明
label2='总投资金额: '+str(touZi[12])
if lostmoney[len(lostmoney)-1]>0:
    colorText='r' #图例说明柱子的颜色
else:
    colorText='g'
plt.bar(day,lostmoney,color=colorText,align='center',width=0.1,label=label1)
plt.legend(loc='best',fontsize='x-large',edgecolor='black')
plt.bar(day,lostmoney,color='r',align='center',width=0.1,label=label2)
plt.legend(loc='best',fontsize='x-large',edgecolor='black')
for i in range(0,len(day)):#如果是负的就是绿柱，正的就是红柱
    if lostmoney[i]>0:
        plt.bar(day[i],lostmoney[i],color='r',align='center',width=0.2)
    else:
        plt.bar(day[i], lostmoney[i], color='g', align='center', width=0.2)

# marker,设置折线的黑点
yLabel = '\n'.join(('持', '有', '亏', '损', '金', '钱'))  # Y轴标题
plt.ylabel(yLabel,
           rotation='horizontal',
           horizontalalignment='right',
           fontsize=20)  # 位置字体大小
plt.xlabel('持有天数', size=20)  # X轴标题
plt.title(changename(x1)+'基金', size=30)  # 主标题
for i in range(0, len(day)):
    plt.annotate(str(allmoney[i]), xy=(day[i], lostmoney[i]),  # 注释内容
                 xytext=(day[i] + day[len(day) - 1] / 100, lostmoney[i] + lostmoney[len(lostmoney) - 1] / 12),
                 # 文本的位置和箭头的位置
                 xycoords='data',
                 # 'data'以被注释的坐标点xy为参考 (默认值)
                 arrowprops=dict(arrowstyle='->', color='red')
                 # 箭头属性
                 )
if lostmoney[len(lostmoney)-1]<0:
    colorText='green'
else:
    colorText='red'
# plt.annotate('投资回报: '+str(lostmoney[len(lostmoney)-1]),size=15,color=colorText,xy=(1,max(lostmoney)))
# plt.annotate('总投资金额: '+str(touZi[12]),size=16,xy=(1,max(lostmoney)-max(lostmoney)/4))#2为两个段文字之间的间隔为两格
plt.grid(True)  # 绘制网格线
plt.plot(day, lostmoney)  # 表格刻度处理
plt.xticks(day)  # X轴刻度细化
if max(lostmoney)>100:
    imgYlabe=math.ceil(max(lostmoney)/10)
    plt.yticks(range(math.ceil(min(lostmoney)), math.ceil(max(lostmoney)) + 10, imgYlabe))
plt.show()  # 图像显示
