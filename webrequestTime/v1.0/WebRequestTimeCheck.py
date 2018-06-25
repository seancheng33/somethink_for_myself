'''
@Author : sean cheng
@Email  : aya234@163.com
@CreateTime   : 2018/6/4
@Program: 功能：测试指定的网址的速度。汕头移动内部OA网使用，不能在公网使用。
          实现方式：使用selenium库和phantomjs做模拟登陆，在requests库中使用selenium登陆后的cookies，
          重新访问页面并计算出响应时间。
'''
import os
import time
import configparser
import requests
from selenium import webdriver

def login_cookies(driver, name, url, config):
    # 通用单点登陆账号
    global_user = config.get('logindata', 'username_global')
    global_pass = config.get('logindata', 'password_global')
    # 财务审计账号
    audit_user = config.get('logindata', 'username_audit')
    audit_pass = config.get('logindata', 'password_audit')
    # 生产中心账号
    sczx_user = config.get('logindata', 'username_sczx')
    sczx_pass = config.get('logindata', 'password_sczx')

    driver.delete_all_cookies()  # 清理掉之前的cookies，后才执行重新的登陆
    if name == '4G业务手续支撑平台':
        driver.get('http://ngid2.st.gmcc.net/contrib/security/pages/Login.aspx')
        driver.implicitly_wait(10)
        driver.find_element_by_xpath('//*[@id="txtUserName"]').send_keys(global_user)
        driver.find_element_by_xpath('//*[@id="txtPassword"]').send_keys(global_pass)
        driver.find_element_by_xpath('//*[@id="btnLogin"]').click()
        driver.implicitly_wait(10)
        driver.find_element_by_xpath('//*[@id="Repeater_ctl00_link"]').click()
        # pass
    elif name == '生产中心':
        driver.get('http://sczx.st.gmcc.net/stms/login.jsp')
        driver.implicitly_wait(10)
        driver.find_element_by_xpath('//*[@id="userId"]').send_keys(sczx_user)
        driver.find_element_by_xpath('//*[@id="password"]').send_keys(sczx_pass)
        driver.find_element_by_xpath('//*[@id="button"]').click()
        # pass
    elif name == '账务稽核平台':
        driver.get('http://audit.st.gmcc.net/login.aspx')
        driver.implicitly_wait(10)
        driver.find_element_by_xpath('//*[@id="txtUserLoginName"]').send_keys(audit_user)
        driver.find_element_by_xpath('//*[@id="txtUserLoginPwd"]').send_keys(audit_pass)
        driver.find_element_by_xpath('//*[@id="btnLogin"]').click()
        # pass
    elif name == '新人力资源门户':
        driver.get('http://iams.st.gmcc.net/login.aspx')
        driver.implicitly_wait(10)
        driver.find_element_by_xpath('//*[@id="tbxLoginID"]').send_keys(global_user)
        driver.find_element_by_xpath('//*[@id="tbxPassword"]').send_keys(global_pass)
        driver.find_element_by_xpath('//*[@id="ImageButton1"]').click()
        # pass
    elif name == '促销工具箱':
        cookies = {  # 促销工具箱的cookies
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
        # driver.add_cookie(cookies)
    else:
        driver.get('http://serms.st.gmcc.net')
        driver.implicitly_wait(10)
        driver.find_element_by_xpath('//*[@id="tbxLoginID"]').send_keys(global_user)
        driver.find_element_by_xpath('//*[@id="tbxPassword"]').send_keys(global_pass)
        driver.find_element_by_xpath('//*[@id="ImageButton1"]').click()

    driver.get(url)
    driver.implicitly_wait(60)
    driver.save_screenshot(name+'.png')  # 截图查看是否为正确的页面

    cookies = {}
    for item in driver.get_cookies():
        cookies[item['name']] = item['value']
    # print(cookies)
    return cookies


def check_web(name, target_url, cookies):
    webpage = requests.get(url=target_url, cookies=cookies)
    if webpage.status_code == 200:
        request_time = webpage.elapsed.total_seconds()  # 获取打开页面的总秒数
        print('站点名称:' + name, '响应时间： ' + str(request_time), '秒')
    else:
        print('站点名称:' + name, '访问异常，状态码：' + str(webpage.status_code))


if __name__ == '__main__':

    config = configparser.ConfigParser()
    config_file = open('config.ini', 'r', encoding='utf-8')
    config.read_file(config_file)

    cap = webdriver.DesiredCapabilities.PHANTOMJS
    cap["phantomjs.page.settings.resourceTimeout"] = 100
    cap["phantomjs.page.settings.userAgent"] = (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36")
    driver = webdriver.PhantomJS(executable_path=os.path.abspath('phantomjs.exe'), desired_capabilities=cap)
    driver.set_window_size(1366, 768)

    web_dict = {
        '行政服务之窗': config.get('website', 'serms'),
        '订餐系统': config.get('website', 'serms2'),
        '新行政服务之窗': config.get('website', 'serwin'),  #
        '新人力资源门户': config.get('website', 'hr'),
        'IT工作台': config.get('website', 'itsm2'),
        '新IT工作台': config.get('website', 'itsm'),
        '综合应用平台': config.get('website', 'iams'),
        '走访管理系统': config.get('website', 'clientvisit'),
        '服务订单系统': config.get('website', 'dmms'),
        '投资一体化项目': config.get('website', 'iimis'),
        '品高工作流': config.get('website', 'newwf'),
        '4G业务手续支撑平台': config.get('website', 'ngid2'),  #
        '统一支撑平台': config.get('website', 'ss'),
        '生产中心': config.get('website', 'sczx'),
        '全业务支撑平台': config.get('website', 'stwed'),
        '营业厅资源管理平台': config.get('website', 'zy'),
        '账务稽核平台': config.get('website', 'audit'),
        '移动渠道信息化系统': config.get('website', 'qd'),
        '促销工具箱': config.get('website', 'cuxiao')
    }

    for key in web_dict:
        urlname = key
        url = web_dict[key]
        cookies = login_cookies(driver, urlname, url, config)
        check_web(urlname, url, cookies)
        #每访问一个站点睡眠3秒
        time.sleep(3)


    driver.quit()

    input('按Enter键退出')