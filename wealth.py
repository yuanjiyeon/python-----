import math  # 用来取整个
import xlrd  # 用来导入表格
import wealthGUI #结果显示界面
import wealthSelectGui#选择界面
# 特殊情况的加减仓
def addmoney( addday, addmon,lost1):
    global y, total,lost
    if i - j + 1 == addday :
        y += addmon
        total += addmon
        lost=lost1 #修正现在有的收益率
baijia = 'bj'  # 百家优选
yifang = 'yf'  # 易方达
guangfaxiaofei = 'gfxf'  #易方达消费
changchengyiliao= 'ccyl' #中欧医疗
x1,mrow=wealthSelectGui.gui()
url = xlrd.open_workbook(r'D:\Github\First\bin\test.xls')  # 打开表格
try:
    aa = url.sheet_by_name(x1)  # 读取其中内容
except:
    print('出错')
nrow = aa.nrows  # 行数
ncol = aa.ncols  # 列数
lilu = aa.col_values(mrow)  # 读取其中的某一列
touZi=aa.col_values(8)
touZ=aa.col_values(9)
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
        addmoney(2,-400,8.5)#错过的加仓
    if x1 == 'yf'and lilu[i-1]!=0:
        addmoney( 61, -200,5)
    if x1 == 'bj'and lilu[i-1]!=0:
        addmoney( 20, 200,0.11)
    if i != len(lilu):  # 读取表格中有空白内容
        if lilu[i] == "":
            break;
wealthGUI.gui(day,lostmoney,allmoney,touZi,touZ,x1)
##
