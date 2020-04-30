import math  # 用来取整个
import xlrd  # 用来导入表格
import numpy as np  # 绘图
import matplotlib as mpl  # 绘图
import matplotlib.pyplot as plt  # 绘图
# 特殊情况的加减仓
def addmoney(jijin, addday, addmon,lost1):
    global y, total,lost

    if jijin == 'yifang' and (i - j + 1 == addday):
        y += addmon
        total += addmon
        lost=lost1 #修正现在有的收益率
    if jijin == 'baijia' and (i - j + 1 == addday):
        y += addmon
        total += addmon  # t
        lost=lost1
#标题改名用
def changename(name):
    if name=='yifang':
       return '易方'
    if name =='baijia':
        return '百家'
baijia = 'baijia'  # 百家优选
yifang = 'yifang'  # 易方
guangfa = 'cc'  # 广发
x1 = yifang
# 用于区分基金进行减仓
mrow = 1# 测试数据 0 是测试数据
url = xlrd.open_workbook(r'D:\Github\First\bin\test.xls')  # 打开表格
aa = url.sheet_by_name(x1)  # 读取其中内容
nrow = aa.nrows  # 行数
ncol = aa.ncols  # 列数
lilu = aa.col_values(mrow)  # 读取其中的某一行
# lilu = ["-0.0003", "-0.0075", "-0.0513", "0.0293", "-0.03","-0.0138","0.038","-0.0570",".0078","-0.0115","0.0032","0.0051","-0.059","0.0169","0.0403","0.0113","-0.0077","-0.0182","0.0049","-0.0052","0.0368","-.01","0.0211","-0.0051","0.004","-.0259","-.0098",".0354","0.0112",".0202","0.0068"]
y = 99.85  # 进场金额，，是扣过0.15%手续费用
i = 0  # 用来纪录天数
j = 0  # 用来统计周末天数
total = 100  # 计算总共投入金额
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
        y += -99.85 * math.ceil(x * 100)
        total += -100 * math.ceil(x * 100)
        if -math.ceil(x * 100) < 1:  # 不足1%，加仓100
            y += 99.85
            total += 100
    if lilu[i] == 0.0:  # 持有天数要去除周末
        j += 1
    print('现金',y,'总投入',total,'利率',lilu[i])
    i += 1
    if lilu[i-1] !=0:
        day.append(i - j)  # 存储
        allmoney.append(total)  # 存储
    if x1 == 'yifang'and lilu[i-1]!=0:
        addmoney('yifang', 6, -200,2)  #基金名称，持仓天数，金额
        addmoney('yifang', 9, -100,3.6)
    if x1 == 'baijia':
        addmoney('baijia', 11, -150,3.5)
        addmoney('baijia',12,-100,4)#没加仓调整亏损
    if i != len(lilu):  # 读取表格中有空白内容
        if lilu[i] == "":
            break;
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
plt.figure(figsize=(30, 50))  # 窗口大小
plt.plot(day, lostmoney, "b--", linewidth=.5, marker='o')  # 绘制折线图
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

plt.grid(True)  # 绘制网格线
plt.plot(day, lostmoney)  # 表格刻度处理
plt.xticks(day)  # X轴刻度细化
if len(day) > 15:
    plt.yticks(range(math.ceil(min(lostmoney)), math.ceil(max(lostmoney)) + 10, 10))
plt.show()  # 图像显示
