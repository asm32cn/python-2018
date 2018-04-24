@echo off

set strName=8080 - Tomcat
set nPort=8080
set strCmd=

for %%k in (allow,block) do (

	rem set strCmd=netsh advfirewall firewall set rule name="%strName%" dir=in protocol=TCP localport=%nPort% new action=%%k
	rem echo #%strCmd%
	rem %strCmd%

	echo #netsh advfirewall firewall set rule name="%strName%" dir=in protocol=TCP localport=%nPort% new action=%%k
	netsh advfirewall firewall set rule name="%strName%" dir=in protocol=TCP localport=%nPort% new action=%%k

	if allow == %%k (
		start /B E:\gitlearn\2\python-2018\py-2018-dev\asm32-buff-sqlite3-web-py.py\asm32-buff-sqlite3-web-py.py
	) else (
		taskkill /IM python.exe /F
	)

	pause
)