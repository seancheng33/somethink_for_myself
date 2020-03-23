#!/bin/bash
################################################################
# 一个修复漏洞的脚本，以下四个漏洞：
# 1、Linux帐户口令生存期
# 2、限制root权限用户远程登录 
# 3、Linux帐户超时自动登出配置 
# 4、Linux未配置账户登录失败锁定
# 修复的方式包括：修改密码过期时间策略
# 添加一个高权限的用户，并且禁止root用户的远程登录
# 设置用户登录超时自动登出，空闲时间为180秒
# 配置账户登录失败锁定，用户登录失败5次就锁定5分钟
################################################################


# 以下的内容为需要检查的各服务器的ip放在双引号里面，用空格分隔
host=("192.168.192.130" "192.168.192.131" "192.168.192.132")
# ssh的用户名
username="root"
# ssh的密码，记得修改密码
password="123456"
# ssh的端口号，如果端口有改变，记得修改端口号
sshport=22

# 检查执行脚本的服务器有没有安装sshpass包
if rpm -q sshpass &>/dev/null
then
    echo "sshpass已经存在，无需安装"
else
    # 如果同目录里面有sshpass的包，就安装，没有则给出提示
	if [ -f "sshpass-1.06-2.el7.x86_64.rpm" ]
	then
        rpm -ivh sshpass-1.06-2.el7.x86_64.rpm
	else
		echo "sshpass包不存在，请确认该rpm包在脚本的目录里面"
		echo "如果服务器支持yum安装，可以执行“yum install sshpass”后再执行本脚本"
		exit
	fi
fi

echo "=====开始漏洞修复进程====="
# 循环多台服务器，执行相同的操作，直接通过sshpass在一台服务器上执行就可以了，不用所有的服务器都登录
for ip in ${host[*]}
do
	# ssh使用-o stricthostkeychecking=no参数是为了跳过某些服务器首次登录需要输入yes/no的确认
	echo "开始执行${ip}的修复进程"
	# 执行以下内容为修复 漏洞:Linux帐户口令生存期策略
	sshpass -p ${password} ssh -p ${sshport} -o stricthostkeychecking=no ${username}@${ip}  'sed -i "/^PASS_MAX_DAYS/c\PASS_MAX_DAYS   90" /etc/login.defs'
	# 执行以下内容为修复 漏洞:限制root权限用户远程登录
	# 添加admin用户
	sshpass -p ${password} ssh -p ${sshport} -o stricthostkeychecking=no ${username}@${ip}  'adduser admin'
	# 修改admin用户的密码为Do1#qaz  如果密码要修改成别的，就替换掉echo空格后面到|之间的字符串
	sshpass -p ${password} ssh -p ${sshport} -o stricthostkeychecking=no ${username}@${ip}  'echo 123456|passwd --stdin admin'
	# 赋权admin用户有root的全部权限
	sshpass -p ${password} ssh -p ${sshport} -o stricthostkeychecking=no ${username}@${ip}  'sed -i "/^root/a\admin    ALL=(ALL)       ALL" /etc/sudoers'
	# 这里的命令执行两遍是因为防止有些配置文件这个选项是注释的，有点配置文件这个选项是打开的。
	sshpass -p ${password} ssh -p ${sshport} -o stricthostkeychecking=no ${username}@${ip}  'sed -i "s/#PermitRootLogin yes/PermitRootLogin no/" /etc/ssh/sshd_config'
	sshpass -p ${password} ssh -p ${sshport} -o stricthostkeychecking=no ${username}@${ip}  'sed -i "s/PermitRootLogin yes/PermitRootLogin no/" /etc/ssh/sshd_config'

	# 执行以下内容为修复  漏洞:Linux帐户超时自动登出配置
	sshpass -p ${password} ssh -p ${sshport} -o stricthostkeychecking=no ${username}@${ip}  'echo 'export TMOUT=180' >>/etc/profile'
	sshpass -p ${password} ssh -p ${sshport} -o stricthostkeychecking=no ${username}@${ip}  'source /etc/profile '

	# 执行以下内容为修复  漏洞:Linux未配置账户登录失败锁定策略
	sshpass -p ${password} ssh -p ${sshport} -o stricthostkeychecking=no ${username}@${ip}  'sed -i "/^auth        required      pam_deny.so/a\auth        required      pam_tally2.so deny=5 unlock_time=300 even_deny_root root_unlock_time=300" /etc/pam.d/password-auth'
	sshpass -p ${password} ssh -p ${sshport} -o stricthostkeychecking=no ${username}@${ip}  'sed -i "/^account     required      pam_permit.so/a\account     required      pam_tally2.so" /etc/pam.d/password-auth'

	# 执行完以上内容后，才执行重启ssh服务，让限制root用户远程登录生效。这个的顺序不要调。放在最后就可以了
	sshpass -p ${password} ssh -p ${sshport} -o stricthostkeychecking=no ${username}@${ip}  'service sshd restart'
done

echo "=====漏洞修复进程成功====="
exit