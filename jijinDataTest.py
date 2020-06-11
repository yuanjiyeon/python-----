import requests
import json
def selectParam(jijin):
      if jijin=='110022':
            params = {
                'callback': 'jQuery18305571026460309254_1591837732526',
                'fundCode': '110022',
                'pageIndex': '1',
                'pageSize': '30',
                'startDate' : '2020-04-01',
                'endDate': '2020-06-10',
                '_': '1591838177370'
            }
      elif jijin=='003095':
          params = {
              'callback': 'jQuery18303586407702383334_1591845298937',
              'fundCode': '003095',
              'pageIndex': '1',
              'pageSize': '30',
              'startDate': '2020-04-01',
              'endDate': '2020-06-10',
              '_': '1591845338804'
          }
      elif jijin=='161903':
          params = {
              'callback': 'jQuery1830816396249439191_1591846172940',
              'fundCode': '161903',
              'pageIndex': '1',
              'pageSize': '30',
              'startDate': '2020-04-01',
              'endDate': '2020-06-10',
              '_': '1591857578727'
          }
      else:
          params = {
              'callback': 'jQuery183040296283814599976_1591858757195',
              'fundCode': '110011',
              'pageIndex': '1',
              'pageSize': '30',
              'startDate': '2020-04-01',
              'endDate': '2020-06-10',
              '_': '1591858777973'
          }
      return params
# 161903---110022---003095----110011
params=selectParam('110022')
hearders={
        'User-Agent' :  'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',
        'Referer'    :  'http://fundf10.eastmoney.com/jjjz_110022.html'
    }
host='http://api.fund.eastmoney.com/f10/lsjz?'
t=requests.get(host,headers=hearders,params=params)
if params['fundCode']=='161903':
    t=t.text[40:-1]
elif params['fundCode']=='110011':
    t=t.text[42:-1]
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