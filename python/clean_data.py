'''
数据清洗，打开excel文件，取出需要的数据后保存为一份txt文档，在另外一个脚本中进行数据汇总。
'''
import xlrd

filename='data/龙湖/龙湖分公司水电费台账及计提2018年2月.xlsx'
book = xlrd.open_workbook(filename)
sheet = book.sheet_by_name('台账')
rows = sheet.nrows

row_list = []

for i in range(1,rows):
    rowdata = sheet.row_values(i)
    try:
        int(rowdata[0])
    except:
        continue
    row_list.append([str(rowdata[0]),str(rowdata[5]),str(rowdata[3]),str(rowdata[12])])

with open('清洗后数据/龙湖/2018年2月.txt','w',encoding='utf-8') as f:
    for item in row_list:
        f.write(','.join(item))
        f.write('\n')

# print(row_list)