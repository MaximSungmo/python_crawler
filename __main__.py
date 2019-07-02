import os
import ssl
import sys
import time

import numpy as np
import pandas as pd
from datetime import datetime
from itertools import count
from urllib.request import Request, urlopen

from bs4 import BeautifulSoup
from selenium import webdriver

from collection import crawler

# 모듈이 실행되고 있는 디렉토리 구하기
BASE_DIR = (os.path.dirname(os.path.abspath(__file__)))
RESULT_DIR = '/home/webmaster/crawling-results/'

def crawling_pelicana():
    # 결과 값을 받는 배열
    results = []

    # range를 지정하지 않고 count를 지정해서 첫 값만 지정해주기
    for page in count(start=1):
        url = 'https://pelicana.co.kr/store/stroe_search.html?page={0}&branch_name=&gu=&si='.format(page)
        # try:
        #     request = Request(url)
        #     ssl._create_default_https_context = ssl._create_unverified_context
        #     resp = urlopen(request)
        #     html = resp.read().decode('utf-8', errors='replace')
        #     print('{0}: success for request [{1}]'.format(datetime.now(), url))
        #
        # except Exception as e:
        #     print('{0} : {1}'.format(e, datetime.now()), file=sys.stderr)
        #     # 에러가 발생하더라도 다음 내용이 진행될 수 있도록 하기 위해서 continue
        #     continue

        html = crawler.crawling(url, encoding='utf-8')

        bs = BeautifulSoup(html, 'html.parser')
        # print(bs.prettify())
        tag_table = bs.find('table', attrs={'class' : 'table mt20'})
        # print(tag_table)
        tag_tbody = tag_table.find('tbody')
        tags_tr = tag_tbody.findAll('tr')
        # page의 마지막 번호를 알아내기
        # 웹사이트에서 마지막 페이지번호에서 tr이 없어지는 것을 확인 후
        if len(tags_tr) == 0:
            break

        for tag_tr in tags_tr:
            # tag들 모두 제외시키고 스트링만 반환시키기, 그 후 리스트로 변경
            strings = list(tag_tr.strings)
            name = strings[1]
            address = strings[3]
            # address에서 시, 도, 구 를 뽑아내서 변수로 저장 추후 사용될 수 있으므로 예시
            sidogu = address.split()[:2]
            tel = strings[5]
            results.append((name, address) + tuple(sidogu))

    # 파일로 저장하기
    # Data frame으로 만들어주기, columns = header
    # df = pd.

    df = pd.DataFrame(results, columns=['name', 'address', 'sido', 'gu'])
    df.to_csv('__results__/pelicana.csv', encoding='utf-8', mode='w', index=True)
    # for t in results:
    #     print(t)

def crawling_nene():
    results = []

    # 마지막 페이지 확인을 위한 임시 변수
    check_page_string = ''

    # range를 지정하지 않고 count를 지정해서 첫 값만 지정해주기
    for page in range(1, 5):
        url = 'https://nenechicken.com/17_new/sub_shop01.asp?ex_select=1&ex_select2=&IndexSword=&GUBUN=A&page={0}'.format(page)

        html = crawler.crawling(url, encoding='utf-8')

        bs = BeautifulSoup(html, 'html.parser')

        # 데이터 변환
        tag_shop_tables = bs.findAll('table', attrs={'class': 'shopTable'})
        # print(tag_shop_tables)
        tag_shop_names = bs.findAll('div', attrs={'class': 'shopName'})
        # print(tag_table)
        tag_shop_addr = bs.findAll('div', attrs={'class': 'shopAdd'})
        shop_lists = zip(tag_shop_names, tag_shop_addr)
        shop_lists = (list(shop_lists))

        # # 마지막 페이지 번호 확인하기
        # if shop_lists[0] == check_page_string:
        #     break
        # else:
        #     check_page_string = shop_lists[0]

        for name, addr in shop_lists:
            # tag들 모두 제외시키고 스트링만 반환시키기, 그 후 리스트로 변경
            name = list(name.strings)[0]
            address = list(addr.strings)[0]
            # address에서 시, 도, 구 를 뽑아내서 변수로 저장 추후 사용될 수 있으므로 예시
            sidogu = address.split()[:2]
            results.append((name, address) + tuple(sidogu))

        # # 마지막 페이지 번호 확인하기(참조함)
        tag_pagination = bs.find('div', attrs={'class', 'pagination'})
        tags_ahref = tag_pagination.findAll('a')
        # 페이지 마지막에 도달한 경우 마지막 <a> 태그의 리스트에는 #으로 처리된 href 값이 들어온다.
        if tags_ahref[-1]['href'] == '#':
            print('break----')
            break

    # 파일로 저장하기
    # Data frame으로 만들어주기, columns = header
    df = pd.DataFrame(results, columns=['name', 'address', 'sido', 'gu'])

    # 모듈이 실행되고 있는 절대 위치 구하기
    print(os.path.abspath(__file__))

    # # 모듈이 실행되고 있는 디렉토리 구하기
    # BASE_DIR = (os.path.dirname(os.path.abspath(__file__)))

    # 저장위치를 현재 모듈이 실행되는 디렉토리에 만들기

    # 저장위치를 변경
    df.to_csv(f'{RESULT_DIR}/__result__/nene.csv', encoding='utf-8', mode='w', index=True)
    # # for t in results:
    #     print(t)


def crawling_kyochon():
    results = []

    for sido1 in range(1, 2):
        # range count로 변경 필요
        for sido2 in range(24, 27):
            url = 'http://www.kyochon.com/shop/domestic.asp?sido1={0}&sido2={1}&txtsearch='.format(sido1, sido2)

            html = crawler.crawling(url, encoding='utf-8')
            # 끝 검출

            if html is None:
                break
            # parser
            bs = BeautifulSoup(html, 'html.parser')
            tag_ul = bs.find('ul', attrs=['class', 'list'])
            tag_span_store_items = tag_ul.findAll('span', attrs=['class', 'store_item'])

            for t in tag_span_store_items:
                strings = list(t.strings)
                # print(strings)
                name = strings[1]
                address = strings[3].replace('\r', '').replace('\t', '').replace('\n', '')
                # address = strings[3].strip('\r\n\t')
                sidogu = address.split()[:2]

                results.append((name, address, tuple(sidogu)))



            print(results)


def store_naver_movie_rank(data):
    for index, div in enumerate(data):
        print(index + 1, div.a.text, sep=":")

# def kyochon_html_parser(html, results):
#     bs = BeautifulSoup(html, 'html.parser')
#     tag_ul = bs.find('ul', attrs=['class', 'list'])
#     tag_span_store_items = tag_ul.findAll('span', attrs=['class', 'store_item'])
#
#     for t in tag_span_store_items:
#         strings = list(t.strings)
#         # print(strings)
#         name = strings[1]
#         address = strings[3].replace('\r', '').replace('\t', '').replace('\n', '')
#         # address = strings[3].strip('\r\n\t')
#         sidogu = address.split()[:2]
#
#         results.append((name, address, tuple(sidogu)))
#
#     return results


def crawling_goobne():
    results=[]
    url='http://goobne.co.kr/store/search_store.jsp'

    # 첫 페이지 로딩
    wd = webdriver.Chrome('E:\program_util\chromedriver_win32\chromedriver.exe')
    wd.get(url)
    time.sleep(3)

    for page in count(1):
        # 자바스크립트 실행
        script='store.getList({0})'.format(page)
        wd.execute_script(script)
        print('{0}: success for request [{1}]'.format(datetime.now(), script))
        time.sleep(3)

        # 실행 결과 HTML(동적으로 렌더링된 HTML) 가져오기
        html = wd.page_source

        # parsing with bs4
        bs = BeautifulSoup(html, 'html.parser')

        tag_tbody = bs.find('tbody', attrs={'id':'store_list'})
        tags_tr = tag_tbody.findAll('tr')

        for tag_tr in tags_tr:
            strings = list(tag_tr.strings)
            name = strings[1]
            address = strings[6]
            sidogu = address.split()[:2]

            results.append((name, address) + tuple(sidogu))

        # 마지막 페이지 번호 확인하기
        next_page = bs.find('li', attrs={'class': 'pager_next'})
        tags_ahref = next_page.findAll('a')
        # 페이지 마지막에 도달한 경우 마지막 <a> 태그의 리스트에는 #으로 처리된 href 값이 들어온다.
        if tags_ahref[-1]['href'] == '#':
            break
    wd.quit()

    df = pd.DataFrame(results, columns=['name', 'address', 'sido', 'gu'])
    df.to_csv('__results__/goobne.csv', encoding='utf-8', mode='w', index=True)

def main():
    # pelicana
    # crawling_pelicana()

    # nene과제
    crawling_nene()

    # kyochon
    # crawling_kyochon()

    # Goobne
    # crawling_goobne()

if __name__ == '__main__':
    main()