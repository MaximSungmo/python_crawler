from bs4 import BeautifulSoup

html = '''
<td class="title">
    <div class="tit3">
	    <a href="/movie/bi/mi/basic.nhn?code=161967" title="기생충">기생충</a>
	</div>
</td>
'''

# 1. tag 조회
def ex1():
    bs = BeautifulSoup(html, 'html.parser')
    # print(bs)
    # print(type(bs))

    # tag = bs.td
    # print(tag)
    # print(type(tag))
    #
    # tag = bs.a
    # print(tag)
    # print(type(tag))

    tag = bs.td.div
    print(tag)
    print(type(tag))

# 2. attributes 값 가져오기
def ex2():
    bs = BeautifulSoup(html, 'html.parser')
    tag = bs.td
    # tag에 td안에 있는 값 중 class에 해당하는 값을 리스트로 출력
    # print(tag['class'])
    # tag = bs.div
    # 값이 없는 경우에는 에러 코드 발생
    # print(tag['id'])
    # print(tag.a.attrs)
    # print(tag.attrs)

# 3. attributes로 태그 조회하기
def ex3():
    bs = BeautifulSoup(html, 'html.parser')
    # td태그를 찾겠다. attrs로 class가 title인 것을
    tag = bs.find('td', attrs={'class':'title'})
    # print(tag)

    tag = bs.find(attrs={'class':'tit3'})
    print(tag)

def main():
    # ex1()
    # ex2()
    ex3()

if __name__ == '__main__':
    main()