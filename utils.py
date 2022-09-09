import urllib.request
import js2py
from bs4 import BeautifulSoup
import json

import config

def getJSON(link) -> dict:
    req = urllib.request.Request(link, headers = config.HEADERS)
    with urllib.request.urlopen(req) as response:
        body = response.read()
    soup = BeautifulSoup(body,'lxml')
    a = soup.select('script')
    # youtube视频信息存在了倒数第五个script脚本内
    js_initial = list(a)[-5].string
    # 将js的JSON对象转成字符串给python读取
    js_code = js_initial + """
        const JSON_String = JSON.stringify(ytInitialData['contents']['twoColumnWatchNextResults']['results']['results']['contents'][0]['videoPrimaryInfoRenderer'])
    """
    # 执行js代码
    context = js2py.EvalJs()
    context.execute(js_code)
    if context.JSON_String:
        result = json.loads(context.JSON_String)
        return result
    else :
        return None

def getLinks() -> list:
    f = open('links.txt','r')
    listsOfLink = f.readlines()
    return listsOfLink
