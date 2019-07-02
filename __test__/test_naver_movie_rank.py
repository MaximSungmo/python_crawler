from urllib.request import Request, urlopen

import pandas as pd
from bs4 import BeautifulSoup

from collection import crawler


def ex01():
    request = Request('http://movie.naver.com/movie/sdb/rank/rmovie.nhn')
    # byte열로 resp 변수에 들어온 상태
    resp = urlopen(request)

    # 네이버에서는 cp949를 사용하여 encoding되어있음 (ms949, euc-kr)
    # 일반적으로 한국 사이트는 utf-8
    html = resp.read().decode('cp949')
    bs = BeautifulSoup(html, 'html.parser')
    # print(bs.prettify())

    # tag를 찾는 법
    divs = bs.findAll('div', attrs={'class':'tit3'})
    # print(divs)
    # 찾은 데이터를 for문으로 돌아가며 콘텐츠를 뽑아내기
    for index, div in enumerate(divs):
        print(index+1, div.a.text, sep=":")


# def ex02():
#     crawler.crawling(
#         url='http://movie.naver.com/movie/sdb/rank/rmovie.nhn',
#         encoding='cp949',
#         proc1=proc_naver_movie_rank,
#         proc2=lambda data: list(map(lambda x: print(x.a.text), data)))


# 크롤링 다수 인자 받을 수 있도록 변경 중
def ex02():
    crawler.crawling(
        url='http://movie.naver.com/movie/sdb/rank/rmovie.nhn',
        encoding='cp949',
        proc1=proc_naver_movie_rank,
        proc2=store_naver_movie_rank)


def proc_naver_movie_rank(data):
    bs = BeautifulSoup(data, 'html.parser')
    results = bs.findAll('div', attrs={'class': 'tit3'})
    return results


def store_naver_movie_rank(data):
    for index, div in enumerate(data):
        print(index + 1, div.a.text, sep=":")


# 두 개의 함수를 메인에서 실행시킬 시, true and false and false
def main():
    ex01()
    ex02()

# __name__ == '__main__' and not ex01() and not ex02()

__name__ == '__main__' and main()





