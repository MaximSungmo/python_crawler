from selenium import webdriver

# selenium 실행
wd = webdriver.Chrome('E:\program_util\chromedriver_win32\chromedriver.exe')

# phantomjs 실행
driver = webdriver.PhantomJS('E:\program_util\phantomjs-2.1.1-windows\\bin\phantomjs.exe')
# 암묵적으로 웹 자원 로드를 위해 3초까지 기다려 준다.
wd.implicitly_wait(3)
wd.get('https://nid.naver.com/nidlogin.login')

'''
URL에 접근하는 api,

get('http://url.com')
페이지의 단일 element에 접근하는 api,

find_element_by_name('HTML_name')
find_element_by_id('HTML_id')
find_element_by_xpath('/html/body/some/xpath')
페이지의 여러 elements에 접근하는 api 등이 있다.

find_element_by_css_selector('#css > div.selector')
find_element_by_class_name('some_class_name')
find_element_by_tag_name('h1')
위 메소드들을 활용시 HTML을 브라우저에서 파싱해주기 때문에 굳이 Python와 BeautifulSoup을 사용하지 않아도 된다.
하지만 Selenium에 내장된 함수만 사용가능하기 때문에 좀더 사용이 편리한 soup객체를 이용하려면 driver.page_source API를 이용해 현재 렌더링 된 페이지의 Elements를 모두 가져올 수 있다.
'''
html = wd.page_source

