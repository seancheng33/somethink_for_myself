@echo off
::演示：删除指定路径下指定天数之前（以文件的最后修改日期为准）的文件。
::如果演示结果无误，把del前面的echo去掉，即可实现真正删除。
::本例调用了临时VBS代码进行日期计算
::本例为兼容不同的日期格式，调用reg命令（XP系统自带）统一设置日期格式，
::处理完毕之后再把日期格式恢复成原来的状态。

rem 指定待删除文件的存放路径
set SrcDir=E:\Program Files (x86)\Syslogd\Logs
rem 指定天数
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