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
        driver.find_element_by_xpath('//*[@id="userId"]').send_keys(global_user)
        driver.find_element_by_xpath('//*[@id="password"]').send_keys(global_pass)
        driver.find_element_by_xpath('//*[@id="button"]').click()
        while 'index' not in driver.current_url:
            driver.get('http://sczx.st.gmcc.net/stms/login.jsp')
            driver.implicitly_wait(10)
            driver.find_element_by_xpath('//*[@id="userId"]').send_keys(global_user)
            driver.find_element_by_xpath('//*[@id="password"]').send_keys(global_pass)
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
    elif name in ('走访管理系统', '全业务支撑平台'):
        driver.get('http://serms.st.gmcc.net')
        driver.implicitly_wait(10)
        driver.find_element_by_xpath('//*[@id="tbxLoginID"]').send_keys(global_user)
        driver.find_element_by_xpath('//*[@id="tbxPassword"]').send_keys(global_pass)
        driver.find_element_by_xpath('//*[@id="ImageButton1"]').click()
    else:
        driver.get('http://eip.gmcc.net/web/gd/customlogin')
        driver.implicitly_wait(3)
        if 'home' in driver.current_url:
            driver.find_element_by_xpath('/html/body/div[2]/div/div/a[2]/span').click()
            driver.implicitly_wait(3)
            driver.find_element_by_xpath('/html/body/div[2]/div/div/div[6]/a').click()
            driver.implicitly_wait(3)
            # 用户名还在，不需要填写。
            driver.find_element_by_xpath('//*[@id="_customlogin_WAR_customloginportlet_jtpwd"]').send_keys(global_pass)
            driver.find_element_by_xpath('//*[@id="_customlogin_WAR_customloginportlet_ldap-login-btn"]').click()
        else:
            driver.find_element_by_xpath('//*[@id="_customlogin_WAR_customloginportlet_login"]').send_keys(global_user)
            driver.find_element_by_xpath('//*[@id="_customlogin_WAR_customloginportlet_jtpwd"]').send_keys(global_pass)
            driver.find_element_by_xpath('//*[@id="_customlogin_WAR_customloginportlet_ldap-login-btn"]').click()

    driver.get(url)
    driver.implicitly_wait(5)
    driver.save_screenshot(name + '.png')  # 截图查看是否为正确的页面

    cookies = {}
    for item in driver.get_cookies():
        cookies[item['name']] = item['value']
    return cookies


def check_web(name, target_url, cookies):
    webpage = requests.get(url=target_url, cookies=cookies)
    if webpage.status_code == 200:
        request_time = webpage.elapsed.total_seconds()  # 获取打开页面的总秒数
        status_txt = '站点名称:' + name + '响应时间： ' + str(request_time) + '秒'
        print(status_txt)
        return status_txt
    else:
        status_txt = '站点名称:' + name + '访问异常，状态码：' + str(webpage.status_code)
        print(status_txt)
        return status_txt

def main():
    config = configparser.ConfigParser()
    config_file = open('config.ini', 'r', encoding='utf-8')
    config.read_file(config_file)

    cap = webdriver.DesiredCapabilities.PHANTOMJS
    cap["phantomjs.page.settings.resourceTimeout"] = 100
    cap["phantomjs.page.settings.userAgent"] = (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36")
    driver = webdriver.PhantomJS(executable_path=os.path.abspath('phantomjs.exe'), desired_capabilities=cap)
    # driver = webdriver.Chrome(executable_path=os.path.abspath('chromedriver.exe'))
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

    status_list = []
    for key in web_dict:
        urlname = key
        url = web_dict[key]
        cookies = login_cookies(driver, urlname, url, config)
        status_txt = check_web(urlname, url, cookies)
        status_list.append(status_txt)
        # 每访问一个站点睡眠3秒
        time.sleep(3)

    driver.quit()

    nowTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    with open(os.path.abspath('status.txt'), 'a', encoding='utf-8') as file:
        file.write('采集时间：' + nowTime + '\n')
        for line in status_list:
            file.write(line)
            file.write('\n')
        file.write('=' * 40 + '\n')


if __name__ == '__main__':
    main()

    # input('按Enter键退出')
