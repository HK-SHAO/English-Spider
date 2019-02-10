from urllib import request
import time
import sys
import re

def getHtml(url):
    page = request.urlopen(url)
    html = page.read()

    t = sys.getfilesystemencoding()
    html = html.decode(t)

    return html

def txt_wrap_by(start_str, end, html):
    start = html.find(start_str)
    if start >= 0:
        start += len(start_str)
        end = html.find(end, start)
        if end >= 0:
            return html[start:end].strip()
    return ''

def trans(word):
    s = ''
    n = 0
    while True:
        html = getHtml('http://dict.youdao.com/w/{}/'.format(word))
        s = txt_wrap_by('<div class="trans-container">', '</ul>', html)
        if len(s) != 0:
            break
        n = n + 1
        if n > 1:
            return '【失败】'
        
        print('【正在重新尝试】')
        time.sleep(15)

    return re.sub('<.+?>', '', s).replace(' ', '').replace('\n','; ')
