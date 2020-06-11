import requests
import json
def selectParam(jijin):#只要改变基金的代码就可以实现查询
    params = {
        'callback': 'jQuery18305571026460309254_1591837732526',#随机
        'fundCode': '110022',#基金代码
        'pageIndex': '1',#页数
        'pageSize': '30',#查询天数
        'startDate': '2020-04-01',#开始日期
        'endDate': '2020-06-10',#结束日期
        '_': '1591838177370'#随机
    }
    params['fundCode']=jijin
    return params
# 161903（百家）---110022（易方达消费）---003095（中欧医疗）----110011（易方达）

params=selectParam(input("输入基金代码"))
hearders={
        'User-Agent' :  'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',
        'Referer'    :  'http://fundf10.eastmoney.com/jjjz_110022.html'
    }
host='http://api.fund.eastmoney.com/f10/lsjz?'
t=requests.get(host,headers=hearders,params=params)
if params['fundCode']=='161903 ':
    t=t.text[40:-1]
else:
    t=t.text[41:-1]
m=json.loads(t)
import xlwt
from xlrd import open_workbook
from xlutils.copy import copy
rb =open_workbook('D:\Github\First\\bin\\t.xls'
                  )
# 括号内参数为表名
wb = copy(rb)#复制
newWs = wb.get_sheet('gfxf');#取sheet表
j=m['Data']['LSJZList'].__len__()
for i in range(0,j):
    data=float(m['Data']['LSJZList'][j-1-i]['JZZZL'])
    print()
    newWs.write(i, 0, format(data/100,'.4f'))
    newWs.write(i,1,m['Data']['LSJZList'][j-1-i]['FSRQ'])
wb.save('D:\Github\First\\bin\\jijin.xlsx')