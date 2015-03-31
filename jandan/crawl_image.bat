@echo off
scrapy crawl imagespider
set /p v=scrapy crawl again? 'y' or 'n':
if "%v%" equ "y" (scrapy crawl imagespider) else exit
pause