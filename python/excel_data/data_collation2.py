'''
将汇总到文件的数据，再进一步的处理
'''
import os,xlsxwriter

id_set = set()
with open('tmp.txt','r',encoding='utf-8') as outfile:
        alldata = outfile.readlines()
        for data in alldata:
            id_set.add(data.split(',')[0])

dict_data = {}

change_dict = {
'2016年1月':201601,
'2016年2月':201602,
'2016年3月':201603,
'2016年4月':201604,
'2016年5月':201605,
'2016年6月':201606,
'2016年7月':201607,
'2016年8月':201608,
'2016年9月':201609,
'2016年10月':201610,
'2016年11月':201611,
'2016年12月':201612,
'2017年1月':201701,
'2017年2月':201702,
'2017年3月':201703,
'2017年4月':201704,
'2017年5月':201705,
'2017年6月':201706,
'2017年7月':201707,
'2017年8月':201708,
'2017年9月':201709,
'2017年10月':201710,
'2017年11月':201711,
'2017年12月':201712,
'2018年1月':201801,
'2018年2月':201802,
}

with open('tmp.txt', 'r', encoding='utf-8') as outfile:
    alldata = outfile.readlines()
    for i in id_set:
        dict_data[i] = {}
    for data in alldata:
        id =  data.split(',')[0]
        # tmp_list = {'name':data.split(',')[2],change_dict[data.split(',')[1]]:data.split(',')[3].strip('\n')}
        if id in id_set:
            dict_data[id]['name']=data.split(',')[2]
            dict_data[id][change_dict[data.split(',')[1]]] = data.split(',')[3].strip('\n')

# for i in id_set:
#     for item in change_dict:
#         if change_dict[item] not in dict_data[i].keys():
#             print(i,dict_data[i]['name'],change_dict[item],'')
#         else:
#             print(i,dict_data[i]['name'],change_dict[item],dict_data[i][change_dict[item]])

filename = '*.xlsx'
workbook = xlsxwriter.Workbook(filename)
worksheet = workbook.add_worksheet('龙湖')
title_list = ['基站编号','基站名称',
              '201601','201602','201603','201604','201605','201606','201607','201608','201609','201610','201611','201612',
              '201701', '201702', '201703', '201704', '201705', '201706', '201707', '201708', '201709', '201710',
              '201711', '201712','201801','201802']
worksheet.write_row('A1',title_list)
num=2
for i in id_set:
    list_tmp = []
    list_tmp.append(i)
    list_tmp.append(dict_data[i]['name'])
    for item in change_dict:
        if change_dict[item] not in dict_data[i].keys():
            list_tmp.append('')
        else:
            list_tmp.append(dict_data[i][change_dict[item]])

    worksheet.write_row('A'+str(num),list_tmp)
    num=int(num)+1