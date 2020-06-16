import matplotlib.pyplot as plt
import math
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
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
def gui(day,lostmoney,allmoney,touZi,touZ,x1):
    plt.figure(figsize=(30, 50))  # 窗口大小
    l=round(lostmoney[len(lostmoney)-1],2)
    label1='投资回报: '+str(l)#增加说明
    label2='总投资金额: '+str(touZi[12])
    label3='基金投资:'+str(touZ[12])
    if lostmoney[len(lostmoney)-1]>0:
        colorText='r' #图例说明柱子的颜色
    else:
        colorText='g'
        #描述内容
    plt.bar(day,lostmoney,color=colorText,align='center',width=0.1,label=label1)
    plt.legend(loc='best',fontsize='x-large',edgecolor='black')
    plt.bar(day,lostmoney,color='r',align='center',width=0.1,label=label3)
    plt.legend(loc='best',fontsize='x-large',edgecolor='black')
    plt.bar(day,lostmoney,color='r',align='center',width=0.1,label=label2)
    plt.legend(loc='best',fontsize='x-large',edgecolor='black')
    for i in range(0,len(day)):#如果是负的就是绿柱，正的就是红柱
        if lostmoney[i]>0:
            plt.bar(day[i],lostmoney[i],color='r',align='center',width=0.2)
        else:
            plt.bar(day[i], lostmoney[i], color='g', align='center', width=0.2)
    yLabel = '\n'.join(('持', '有', '亏', '损', '金', '钱'))  # Y轴标题
    plt.ylabel(yLabel,
               rotation='horizontal',#字体方向
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
    plt.plot(day, lostmoney,'-p')  # 折线
    plt.xticks(day)  # X轴刻度细化
    if max(lostmoney)>100:#Y轴刻度细化
        imgYlabe=math.ceil(max(lostmoney)/10)
        plt.yticks(range(math.ceil(min(lostmoney)), math.ceil(max(lostmoney)) + 10, imgYlabe))
    plt.show()  # 图像显示#
