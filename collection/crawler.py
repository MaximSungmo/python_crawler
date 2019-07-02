# crawler.py module
import ssl
import sys
from urllib.request import Request, urlopen

from datetime import datetime


def crawling(
        url=' ',
        encoding='utf-8',
        err=lambda e: print('{0} : {1}'.format(e, datetime.now()), file=sys.stderr),
        proc1=lambda data: data,
        proc2=lambda data: data
        ):

    try:
        request = Request(url)
        ssl._create_default_https_context = ssl._create_unverified_context
        print('{0}: success for request [{1}]'.format(datetime.now(), url))
        results = proc2(proc1(urlopen(request).read().decode(encoding, errors='replace')))

    except Exception as e:
        err(e)
        return None

    return results


def test(*procs):
    procse = list(map(lambda data: data, procs))
    print(procse[0])
    return
