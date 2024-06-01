@echo off

pyinstaller -F main.py -n mkbat

python main.py dist\mkbat.exe -n mkbat -c "@python D:\Apps\mkbat\main.py %*"