@echo off
::��ʾ��ɾ��ָ��·����ָ������֮ǰ�����ļ�������޸�����Ϊ׼�����ļ���
::�����ʾ������󣬰�delǰ���echoȥ��������ʵ������ɾ����
::������������ʱVBS����������ڼ���
::����Ϊ���ݲ�ͬ�����ڸ�ʽ������reg���XPϵͳ�Դ���ͳһ�������ڸ�ʽ��
::�������֮���ٰ����ڸ�ʽ�ָ���ԭ����״̬��

rem ָ����ɾ���ļ��Ĵ��·��
set SrcDir=E:\Program Files (x86)\Syslogd\Logs
rem ָ������
set DaysAgo=7
for /f "delims=" %%a in ('reg query "HKEY_CURRENT_USER\Control Panel\International" /v sShortDate') do (
    set "RegDateOld=%%a"
)
set RegDateOld=%RegDateOld:~-8%
reg add "HKEY_CURRENT_USER\Control Panel\International" /v sShortDate /t REG_SZ /d yyyy-M-d /f>nul
>"%temp%\DstDate.vbs" echo LastDate=date()-%DaysAgo%
>>"%temp%\DstDate.vbs" echo FmtDate=right(year(LastDate),4) ^& right("0" ^& month(LastDate),2) ^& right("0" ^& day(LastDate),2)
>>"%temp%\DstDate.vbs" echo wscript.echo FmtDate
for /f %%a in ('cscript /nologo "%temp%\DstDate.vbs"') do (
    set "DstDate=%%a"
)
set DstDate=%DstDate:~0,4%-%DstDate:~4,2%-%DstDate:~6,2%
for /r "%SrcDir%" %%a in (*.*) do (
    if "%%~ta" leq "%DstDate%" (
        if exist "%%a" (
            del /f /q "%%a"
        )
    )
)
reg add "HKEY_CURRENT_USER\Control Panel\International" /v sShortDate /t REG_SZ /d %RegDateOld% /f>nul
pause