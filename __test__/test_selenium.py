import time

from selenium import webdriver

# selenium crome driver 실행
wd = webdriver.Chrome('E:\program_util\chromedriver_win32\chromedriver.exe')
wd.get('http://www.google.com')

time.sleep(2)
# 연결된 페이지의 html 정보 모두 가져오기
html = wd.page_source
print(html)
wd.quit()
