'''零时执行补全最后一点资料版'''
import re,csv,os,sys,time,shutil

#分隔数据功能
def split_data(data,writer,writer2):
    for line in data:
        split1 = line.split('\t')
        # ['2017-10-31 23:59:20','User.Info','10.245.128.242',
        # 'Oct 31 23:56:00 RT_FLOW: RT_FLOW_SESSION_CLOSE: session closed unset: 10.245.242.251/51193->10.251.139.241/53 junos-dns-udp 10.245.242.251/51193->10.251.139.241/53 None None 17 SGS-DDI-13 Trust InterBusiness 80240055 1(72) 1(125) 59 UNKNOWN UNKNOWN N/A(N/A) reth0.1\n']
        split2 = split1[3].replace('  ',' ').split(' ')
        # ['Oct', '31', '23:56:00',
        # 'RT_FLOW: RT_FLOW_SESSION_CLOSE: session closed unset: 10.245.242.251/51193->10.251.139.241/53 junos-dns-udp 10.245.242.251/51193->10.251.139.241/53 None None 17 SGS-DDI-13 Trust InterBusiness 80240055 1(72) 1(125) 59 UNKNOWN UNKNOWN N/A(N/A) reth0.1\n']
        split3 = ' '.join(split2[5:])
        # ['RT_FLOW: RT_FLOW_SESSION_CLOSE: session closed unset: 10.245.242.251',
        # '51193-', '10.251.139.241', '53 junos-dns-udp 10.245.242.251', '51193-', '10.251.139.241',
        # '53 None None 17 SGS-DDI-13 Trust InterBusiness 80240055 1(72) 1(125) 59 UNKNOWN UNKNOWN N', 'A(N', 'A) reth0.1\n']
        split4 = re.split('[\>]+', split3)
        # ['RT_FLOW:', 'RT_FLOW_SESSION_CLOSE:', 'session', 'closed', 'unset:', '10.245.242.251']
        split5 = split4[0].split(' ')
        # ['53', 'junos-dns-udp', '10.245.242.251']

        data1 = split1[0]
        data2 = split1[1]
        data3 = split1[2]
        data4 = split2[0] + ' ' + split2[1] + ' ' + split2[2]
        data5 = split2[3] + ' ' + split2[4]
        if data2 == 'User.Info':
            split6 = split4[1].split(' ')
            split7 = re.split('[/\-]+', split5[-1])
            split8 = split6[0].split('/')
            data6 = ' '.join(split5[:-1])
            data7 = split7[0]
            data8 = split7[1]
            data9 = split8[0]
            data10 = split8[1]
            # print(split6)
            # 接下来的数据分隔需要做判断情况了
            if data5 == "RT_FLOW: RT_FLOW_SESSION_DENY:":
                # print('deny')
                data11 = ' '
                data12 = ' '
                data13 = ' '
                data14 = ' '
                data15 = ' '
                data16 = split6[2]
                data17 = split6[4]
                data18 = split6[5]
                data19 = split6[6]
                data20 = ' '.join(split6[8:]).replace('\n','')
                writer.writerow([data1, data2, data3, data4, data5, data6, data7, data8, data9, data10, data11,
                    data12, data13,data14, data15, data16, data17, data18,data19, data20])
            else:
                data11 = split6[1]
                split9 = re.split('[/\-]+', split6[2])
                # ['10.245.242.251', '51193', '']
                data12 = split9[0]
                data13 = split9[1]
                split10 = split4[-1].split(' ')
                # ['10.251.139.241/53', 'None', 'None', '17', 'SGS-DDI-13', 'Trust', 'InterBusiness', '80240055', '1(72)', '1(125)', '59', 'UNKNOWN', 'UNKNOWN', 'N/A(N/A)', 'reth0.1']
                split11 = split10[0].split('/')
                data14 = split11[0]
                data15 = split11[1]
                data16 = split10[3]
                data17 = split10[4]
                data18 = split10[5]
                data19 = split10[6]
                data20 = ' '.join(split10[8:]).replace('\n','')
                writer.writerow([data1, data2, data3, data4, data5, data6, data7, data8, data9, data10, data11,
                    data12, data13,data14,data15, data16, data17, data18,data19, data20])
        else:
            data6 = ' '.join(split2[3:]).replace(',',' ').replace('\n','')    
            writer2.writerow([data1, data2, data3, data4, data5, data6])
            
def beforeDate():
    #计算天数
    now = time.time()
    n = 2 #
    before = now - n * 24 * 3600  # 可以改变n 的值计算n天前的
    #date = time.strftime("%Y%m%d", time.localtime(now))
    beforeDate = time.strftime("%Y-%m-%d", time.localtime(before))
    return beforeDate

now = time.time()
n = 1 #
before = now - n * 24 * 3600  # 可以改变n 的值计算n天前的
#date = time.strftime("%Y%m%d", time.localtime(now))
yestoday = time.strftime("%Y-%m-%d", time.localtime(before))

file_name = 'SyslogCatchAll-2017-12-06.txt'
base_dir = 'E:\\LoggerSplit\\' # 基础路径，生成的文件和文件夹的基础路径
file_dir = base_dir+time.strftime('%Y-%m-%d', time.localtime(time.time())) #每天生成的文件夹的名称

file = open(file_name,'r')
data = file.readlines()
if not os.path.exists(file_dir):
    if not os.path.exists(base_dir):
        os.makedirs(file_dir)
    else:
        os.mkdir(file_dir+'\\')
    #在创建文件夹的时候，删除两天前的文件夹,基础路径加前天的日期，等于前天的路径
    before_day = base_dir+beforeDate()
    if os.path.exists(before_day):
        shutil.rmtree(before_day)
#计算文件夹中的文件数，实现新增加文件的名称是递增
ls = os.listdir(file_dir)
count = 0
for i in ls:
    if os.path.isfile(os.path.join(file_dir, i))and str(i).find('info'):
        count += 1
#建立新csv文件，保存分隔后的数据
csvfile = open(os.path.join(file_dir,'info'+str(count+1)+'.csv'),'w',encoding='utf-8',newline='')
writer = csv.writer(csvfile)
csvfile2 = open(os.path.join(file_dir,'error'+str(count+1)+'.csv'),'w',encoding='utf-8',newline='')
writer2 = csv.writer(csvfile2)
#执行分隔数据功能
split_data(data,writer,writer2)

#关闭文件
csvfile.close()
csvfile2.close()
file.close()

