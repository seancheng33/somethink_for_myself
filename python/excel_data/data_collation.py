'''
将另外一个脚本的清洗后的数据进行汇总到一个文件。
'''
import os

base_dir = '清洗后数据/龙湖/'
file_list = os.listdir(base_dir)

final_data =[]
for filename in file_list:
    with open(os.path.join(base_dir,filename),'r',encoding='utf-8') as of:
        all_data = of.readlines()
        for data in all_data:
            tmp_list =[]
            tmp_data =data.split(',')
            if tmp_data[1] == '':
                continue
            tmp_list.append(tmp_data[1])
            tmp_list.append(filename.split('.')[0])
            tmp_list.append(tmp_data[2])
            tmp_list.append(tmp_data[3])
            final_data.append(tmp_list)

with open('tmp.txt','w',encoding='utf-8') as infile:
    for item in final_data:
        infile.write(','.join(item))