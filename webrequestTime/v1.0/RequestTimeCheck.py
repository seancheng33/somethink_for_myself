'''
@Author : sean cheng
@Email  : aya234@163.com
@CreateTime   : 2018/5/31
@Program: 测试指定的网址的速度。汕头移动内部OA网使用，不能在公网使用。
'''

import requests


# 使用cookies登录，获取页面状态
def check_web(name, target_url):
    cookie1 = {  # 多数站点可以用的cookies
        '__STIAMS-Passport__': 'baeiibafMs2%3aB%3a%3f849F%3fMMyq!',
        'ST___STMOBILE-SER___IAPAppCookie':
            'Tyq!%24%24+0q!!0s%40%40%3c%3a6DTMbaeiibafMs2%3aB%3a%3f849F%3fM00%24%25%7d+ry%7cu%5d%24u%2300Mb%60ah_e_caPadjafjd%60',
        'ASP.NET_SessionId': 'jspoztmtxzw0jsqewp152k55',
        'ST___STMOBILE-HRM___IAPAppCookie':
            'Tyq!%24%24+0q!!0s%40%40%3c%3a6DTMbaeiibafMs2%3aB%3a%3f849F%3fM00%24%25%7d+ry%7cu%5dx%23%7d00Mb%60ah_e_caPaejagjaf',
        'ST_IAP_FlagCookie':
            'Tyq!%24%24+0v%3d280s%40%40%3c%3a6DTMbaeiibafMs2%3aB%3a%3f849F%3fM00%24%25%7d+ry%7cu%5dx%23%7d00Mb%60ah_e_caPaejagjaf'
    }

    cookie2 = {  # 促销工具箱的cookies
        '__STIAMS-Passport__': 'baeiibafMs2%3aB%3a%3f849F%3fMMyq!',
        'ST___STMOBILE-SER___IAPAppCookie':
            'Tyq!%24%24+0q!!0s%40%40%3c%3a6DTMbaeiibafMs2%3aB%3a%3f849F%3fM00%24%25%7d+ry%7cu%5d%24u%2300Mb%60ah_e_caPadjafjd%60',
        'ST___STMOBILE-HRM___IAPAppCookie':
            'Tyq!%24%24+0q!!0s%40%40%3c%3a6DTMbaeiibafMs2%3aB%3a%3f849F%3fM00%24%25%7d+ry%7cu%5dx%23%7d00Mb%60ah_e_caPaejagjaf',
        'ST___STMOBILE-SM___IAPAppCookie':
            'Tyq!%24%24+0q!!0s%40%40%3c%3a6DTMbaeiibafMs2%3aB%3a%3f849F%3fM00%24%25%7d+ry%7cu%5d%24%7d00Mb%60ah_e_caPaejdgjbf',
        'ST___STMOBILE-ITSM2___IAPAppCookie':
            'Tyq!%24%24+0q!!0s%40%40%3c%3a6DTMbaeiibafMs2%3aB%3a%3f849F%3fM00%24%25%7d+ry%7cu%5dy%25%24%7db00Mb%60ah_e_caPafjcfjcc',
        'ST___STMOBILE-VISITGIS___IAPAppCookie':
            "Tyq!%24%24+0q!!0s%40%40%3c%3a6DTMbaeiibafMs2%3aB%3a%3f849F%3fM00%24%25%7d+ry%7cu%5d'y%24y%25wy%2400Mb%60ah_e_caPafjchjah",
        'ST___STMOBILE-DMMS___IAPAppCookie':
            'Tyq!%24%24+0q!!0s%40%40%3c%3a6DTMbaeiibafMs2%3aB%3a%3f849F%3fM00%24%25%7d+ry%7cu%5dt%7d%7d%2400Mb%60ah_e_caPafjchjdg',
        'ST___STMOBILE-TIIMIS___IAPAppCookie':
            'Tyq!%24%24+0q!!0s%40%40%3c%3a6DTMbaeiibafMs2%3aB%3a%3f849F%3fM00%24%25%7d+ry%7cu%5d%25yy%7dy%2400Mb%60ah_e_caPafjcij%60a',
        'ST___STMOBILE-NEWWF___IAPAppCookie':
            'Tyq!%24%24+0q!!0s%40%40%3c%3a6DTMbaeiibafMs2%3aB%3a%3f849F%3fM00%24%25%7d+ry%7cu%5d%7eu((v00Mb%60ah_e_caPafjdajae; pac-username=caiqingchun',
        'metro_UserInfo':
            '%7B%22horizontal%22%3A1%2C%22vertical%22%3A1%2C%22MetroLayoutGuid%22%3A%22107bb806-0b24-487f-a192-3d4d802dc909%22%2C%22WorkType%22%3A2%2C%22UserID%22%3A%2221575145%22%2C%22LoginID%22%3A%22luxiaochun%22%2C%22NGBossID%22%3A%22DST001HL0001%22%2C%22UserName%22%3A%22%E5%8D%A2%E6%99%93%E7%BA%AF%22%2C%22Email%22%3A%22luxiaochun%40st.gd.chinamobile.com%22%2C%22Mobile%22%3A%2213502988222%22%2C%22TelephoneNumber%22%3A%22%22%2C%22DPID%22%3A%22220114167572%22%2C%22DPName%22%3A%22%E7%BA%A2%E9%A2%86%E5%B7%BE%E8%90%A5%E4%B8%9A%E5%8E%85%22%2C%22ParentDPID%22%3A%22220114163171%22%2C%22ParentDPIDName%22%3A%22%E6%B8%A0%E9%81%93%E8%BF%90%E8%90%A5%E4%B8%AD%E5%BF%83%22%2C%22DPFullName%22%3A%22%E6%B8%A0%E9%81%93%E8%BF%90%E8%90%A5%E4%B8%AD%E5%BF%83%3E%E7%BA%A2%E9%A2%86%E5%B7%BE%E8%90%A5%E4%B8%9A%E5%8E%85%22%2C%22POS%22%3A%2250%22%2C%22POSName%22%3A%22%E5%BA%97%E9%9D%A2%E7%BB%8F%E7%90%86%22%2C%22JobTypeID%22%3A%22%E5%BA%97%E9%9D%A2%E7%BB%8F%E7%90%86(%E4%B8%AD%E7%BA%A7%E4%B8%93%E5%91%98%E7%BA%A7)%22%2C%22NGBosses%22%3A%5B%7B%22NGBossID%22%3A%22DST001HL0001%22%2C%22ChannelCoding%22%3A%22%22%2C%22AccessControl%22%3A%22%22%2C%22DPID%22%3A%22220114167572%22%2C%22DPName%22%3A%22%E7%BA%A2%E9%A2%86%E5%B7%BE%E8%90%A5%E4%B8%9A%E5%8E%85%22%7D%2C%7B%22NGBossID%22%3A%22DST001SL0014%22%2C%22ChannelCoding%22%3A%22%22%2C%22AccessControl%22%3A%22%22%2C%22DPID%22%3A%22220114163187%22%2C%22DPName%22%3A%22%E6%B1%95%E6%A8%9F%E8%90%A5%E4%B8%9A%E5%8E%85%22%7D%2C%7B%22NGBossID%22%3A%22DST001SL0014%22%2C%22ChannelCoding%22%3A%22%22%2C%22AccessControl%22%3A%22%22%2C%22DPID%22%3A%22220114167588%22%2C%22DPName%22%3A%22%E5%85%A8%E7%90%83%E9%80%9A%E8%90%A5%E4%B8%9A%E5%8E%85%22%7D%5D%2C%22UserRoless%22%3A%5B%7B%22RoleName%22%3A%22%E7%B3%BB%E7%BB%9F%E7%AE%A1%E7%90%86%E5%91%98%22%2C%22RoleCode%22%3A%22025%22%7D%2C%7B%22RoleName%22%3A%22%E5%B8%82%E5%85%AC%E5%8F%B8%E7%AE%A1%E7%90%86%E5%91%98%22%2C%22RoleCode%22%3A%22002%22%7D%2C%7B%22RoleName%22%3A%22%E5%88%86%E5%85%AC%E5%8F%B8%E7%AE%A1%E7%90%86%E5%91%98%22%2C%22RoleCode%22%3A%22038%22%7D%5D%2C%22AuthID%22%3Anull%2C%22Domain%22%3Anull%7D',
        'ST___STMOBILE-QD___IAPAppCookie':
            'Tyq!%24%24+0q!!0s%40%40%3c%3a6DTMbaeiibafMs2%3aB%3a%3f849F%3fM00%24%25%7d+ry%7cu%5d%22t00Mb%60ah_e_caPafjdejah',
        'ST_IAP_FlagCookie':
            'Tyq!%24%24+0v%3d280s%40%40%3c%3a6DTMbaeiibafMs2%3aB%3a%3f849F%3fM00%24%25%7d+ry%7cu%5d%22t00Mb%60ah_e_caPafjdejah',
        'ASP.NET_SessionId': 'z343qfozter3qzgsbq24sk0h'
    }

    cookie3 = {  # 生产中心的cookies
        'JSESSIONID': '805E4B1A7A1F098F2DD6862D3A53AEF6',
        '__STIAMS-Passport__': 'baeiibafMs2%3aB%3a%3f849F%3fMMyq!',
        'ST___STMOBILE-SER___IAPAppCookie':
            'Tyq!%24%24+0q!!0s%40%40%3c%3a6DTMbaeiibafMs2%3aB%3a%3f849F%3fM00%24%25%7d+ry%7cu%5d%24u%2300Mb%60ah_e_caPadjafjd%60',
        'ST___STMOBILE-HRM___IAPAppCookie':
            'Tyq!%24%24+0q!!0s%40%40%3c%3a6DTMbaeiibafMs2%3aB%3a%3f849F%3fM00%24%25%7d+ry%7cu%5dx%23%7d00Mb%60ah_e_caPaejagjaf',
        'ST___STMOBILE-SM___IAPAppCookie':
            'Tyq!%24%24+0q!!0s%40%40%3c%3a6DTMbaeiibafMs2%3aB%3a%3f849F%3fM00%24%25%7d+ry%7cu%5d%24%7d00Mb%60ah_e_caPaejdgjbf',
        'ST___STMOBILE-ITSM2___IAPAppCookie':
            'Tyq!%24%24+0q!!0s%40%40%3c%3a6DTMbaeiibafMs2%3aB%3a%3f849F%3fM00%24%25%7d+ry%7cu%5dy%25%24%7db00Mb%60ah_e_caPafjcfjcc',
        'ST___STMOBILE-VISITGIS___IAPAppCookie':
            "Tyq!%24%24+0q!!0s%40%40%3c%3a6DTMbaeiibafMs2%3aB%3a%3f849F%3fM00%24%25%7d+ry%7cu%5d'y%24y%25wy%2400Mb%60ah_e_caPafjchjah",
        'ST___STMOBILE-DMMS___IAPAppCookie':
            'Tyq!%24%24+0q!!0s%40%40%3c%3a6DTMbaeiibafMs2%3aB%3a%3f849F%3fM00%24%25%7d+ry%7cu%5dt%7d%7d%2400Mb%60ah_e_caPafjchjdg',
        'ST___STMOBILE-TIIMIS___IAPAppCookie':
            'Tyq!%24%24+0q!!0s%40%40%3c%3a6DTMbaeiibafMs2%3aB%3a%3f849F%3fM00%24%25%7d+ry%7cu%5d%25yy%7dy%2400Mb%60ah_e_caPafjcij%60a',
        'ST___STMOBILE-NEWWF___IAPAppCookie':
            'Tyq!%24%24+0q!!0s%40%40%3c%3a6DTMbaeiibafMs2%3aB%3a%3f849F%3fM00%24%25%7d+ry%7cu%5d%7eu((v00Mb%60ah_e_caPafjdajae; pac-username=caiqingchun',
        'metro_UserInfo':
            '%7B%22horizontal%22%3A1%2C%22vertical%22%3A1%2C%22MetroLayoutGuid%22%3A%22107bb806-0b24-487f-a192-3d4d802dc909%22%2C%22WorkType%22%3A2%2C%22UserID%22%3A%2221575145%22%2C%22LoginID%22%3A%22luxiaochun%22%2C%22NGBossID%22%3A%22DST001HL0001%22%2C%22UserName%22%3A%22%E5%8D%A2%E6%99%93%E7%BA%AF%22%2C%22Email%22%3A%22luxiaochun%40st.gd.chinamobile.com%22%2C%22Mobile%22%3A%2213502988222%22%2C%22TelephoneNumber%22%3A%22%22%2C%22DPID%22%3A%22220114167572%22%2C%22DPName%22%3A%22%E7%BA%A2%E9%A2%86%E5%B7%BE%E8%90%A5%E4%B8%9A%E5%8E%85%22%2C%22ParentDPID%22%3A%22220114163171%22%2C%22ParentDPIDName%22%3A%22%E6%B8%A0%E9%81%93%E8%BF%90%E8%90%A5%E4%B8%AD%E5%BF%83%22%2C%22DPFullName%22%3A%22%E6%B8%A0%E9%81%93%E8%BF%90%E8%90%A5%E4%B8%AD%E5%BF%83%3E%E7%BA%A2%E9%A2%86%E5%B7%BE%E8%90%A5%E4%B8%9A%E5%8E%85%22%2C%22POS%22%3A%2250%22%2C%22POSName%22%3A%22%E5%BA%97%E9%9D%A2%E7%BB%8F%E7%90%86%22%2C%22JobTypeID%22%3A%22%E5%BA%97%E9%9D%A2%E7%BB%8F%E7%90%86(%E4%B8%AD%E7%BA%A7%E4%B8%93%E5%91%98%E7%BA%A7)%22%2C%22NGBosses%22%3A%5B%7B%22NGBossID%22%3A%22DST001HL0001%22%2C%22ChannelCoding%22%3A%22%22%2C%22AccessControl%22%3A%22%22%2C%22DPID%22%3A%22220114167572%22%2C%22DPName%22%3A%22%E7%BA%A2%E9%A2%86%E5%B7%BE%E8%90%A5%E4%B8%9A%E5%8E%85%22%7D%2C%7B%22NGBossID%22%3A%22DST001SL0014%22%2C%22ChannelCoding%22%3A%22%22%2C%22AccessControl%22%3A%22%22%2C%22DPID%22%3A%22220114163187%22%2C%22DPName%22%3A%22%E6%B1%95%E6%A8%9F%E8%90%A5%E4%B8%9A%E5%8E%85%22%7D%2C%7B%22NGBossID%22%3A%22DST001SL0014%22%2C%22ChannelCoding%22%3A%22%22%2C%22AccessControl%22%3A%22%22%2C%22DPID%22%3A%22220114167588%22%2C%22DPName%22%3A%22%E5%85%A8%E7%90%83%E9%80%9A%E8%90%A5%E4%B8%9A%E5%8E%85%22%7D%5D%2C%22UserRoless%22%3A%5B%7B%22RoleName%22%3A%22%E7%B3%BB%E7%BB%9F%E7%AE%A1%E7%90%86%E5%91%98%22%2C%22RoleCode%22%3A%22025%22%7D%2C%7B%22RoleName%22%3A%22%E5%B8%82%E5%85%AC%E5%8F%B8%E7%AE%A1%E7%90%86%E5%91%98%22%2C%22RoleCode%22%3A%22002%22%7D%2C%7B%22RoleName%22%3A%22%E5%88%86%E5%85%AC%E5%8F%B8%E7%AE%A1%E7%90%86%E5%91%98%22%2C%22RoleCode%22%3A%22038%22%7D%5D%2C%22AuthID%22%3Anull%2C%22Domain%22%3Anull%7D',
        'ST___STMOBILE-QD___IAPAppCookie':
            'Tyq!%24%24+0q!!0s%40%40%3c%3a6DTMbaeiibafMs2%3aB%3a%3f849F%3fM00%24%25%7d+ry%7cu%5d%22t00Mb%60ah_e_caPafjdejah',
        'ST_IAP_FlagCookie': 'Tyq!%24%24+0v%3d280s%40%40%3c%3a6DTMbaeiibafMs2%3aB%3a%3f849F%3fM00%24%25%7d+ry%7cu%5d%22t00Mb%60ah_e_caPafjdejah'
    }

    cookie4 = {  # 账务稽核平台的cookies
        'ASP.NET_SessionId': 'd3w34ca5jfs1wqezniqa2mwj'
    }

    if name == '促销工具箱':
        # 促销工具箱需要用另外的cookies登陆
        webpage = requests.get(url=target_url, cookies=cookie2)
        # print(webpage.text)  # 打印页面源码，了解访问的页面情况
    elif name == '生产中心':
        webpage = requests.get(url=target_url, cookies=cookie3)
        # print(webpage.text)  # 打印页面源码，了解访问的页面情况
    elif name == '4G业务手续支撑平台':
        # 只能用ie登陆，使用完整包含cookies的headers
        headers = {
            'Accept': 'text/html, application/xhtml+xml, image/jxr, */*',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-Hans-CN, zh-Hans; q=0.5',
            'Cookie': 'ASP.NET_SessionId=hckvksgtko1aoxbifgz5tke1; {83CC3CC5-10B3-419e-97DA-B0172B10AAC7}=hB16KOmJCYgXEC4+WBi/bQ==; {5E73B429-3E4A-43EB-9A34-05EFAE8C5DC1}=Caiqingchun',
            'Host': 'ngid2.st.gmcc.net',
            'Proxy-Connection': 'Keep-Alive',
            'Upgrade-Insecure-Requests': '1',
            'Referer': 'http://ngid2.st.gmcc.net/contrib/security/pages/Login.aspx',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko'
        }
        cookies = {
            'ASP.NET_SessionId': 'hckvksgtko1aoxbifgz5tke1',
            '{83CC3CC5-10B3-419e-97DA-B0172B10AAC7}': 'hB16KOmJCYgXEC4+WBi/bQ==',
            '{5E73B429-3E4A-43EB-9A34-05EFAE8C5DC1}': 'Caiqingchun'
        }
        # webpage = requests.get(url=target_url, headers=headers)
        webpage = requests.get(url=target_url, cookies=cookies)
        # print(webpage.text)  # 打印页面源码，了解访问的页面情况
    elif name == '账务稽核平台':
        webpage = requests.get(url=target_url, cookies=cookie4)
        # print(webpage.text)  # 打印页面源码，了解访问的页面情况
    else:
        webpage = requests.get(url=target_url, cookies=cookie1)
        # print(webpage.text)  # 打印页面源码，了解访问的页面情况

    # 如果返回的是200的状态码，才后续执行。
    if webpage.status_code == 200:
        request_time = webpage.elapsed.total_seconds()  # 获取打开页面的总秒数
        print('站点名称:' + name, '响应时间： ' + str(request_time), '秒')
    else:
        print('站点名称:' + name, '访问异常，状态码：' + str(webpage.status_code))


if __name__ == '__main__':
    # 定义网址的字典
    web_dict = {
        '行政服务之窗': 'http://serms.st.gmcc.net/logistics/main.aspx',
        '订餐系统': 'http://serms.st.gmcc.net/serms/orderdish/mainform.aspx',
        '新行政服务之窗': 'http://serwin.st.gmcc.net',  #
        '新人力资源门户': 'http://hr.st.gmcc.net/Common/SalaryService.ashx',
        'IT工作台': 'http://itsm2.st.gmcc.net/STITPaltform/UsedIndex.aspx',
        '新IT工作台': 'http://itsm.st.gmcc.net',
        '综合应用平台': 'http://iams.st.gmcc.net',
        '走访管理系统': 'http://clientvisit.st.gmcc.net',
        '服务订单系统': 'http://dmms.st.gmcc.net',
        '投资一体化项目': 'http://iimis.st.gmcc.net/Modules/MyWork/MyToDo.html?r=0.621052226183886',
        '品高工作流': 'http://newwf.st.gmcc.net/Modules/Workflow/ToDoListNavigation.aspx',
        '4G业务手续支撑平台': 'http://ngid2.st.gmcc.net/Modules/MyWorkBench/MyTodos.aspx',  #
        '统一支撑平台': 'http://ss.st.gmcc.net/Sys/SystemFunction/FixedBlock.html',
        '生产中心': 'http://sczx.st.gmcc.net/stms/system/index.action',
        '全业务支撑平台': 'http://stwed.st.gmcc.net/stdwdb',
        '营业厅资源管理平台': 'http://zy.st.gmcc.net/iFrameWork/Test/Default.htm',
        '账务稽核平台': 'http://audit.st.gmcc.net/Index.aspx',
        '移动渠道信息化系统': 'http://qd.st.gmcc.net/Web/default.aspx',
        '促销工具箱': 'http://cuxiao.st.gmcc.net/c/DefaultIndex.aspx'
    }

    # 循环执行字典中的内容
    for key in web_dict:
        urlname = key
        url = web_dict[key]
        check_web(urlname, url)

    input('按Enter键退出')
