import urllib.request
import urllib.parse
import json
import time

while True:
    content = input("请输入需要翻译的内容(输入'q!'退出程序)：")
    if content == 'q!':
        break
    url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule"

    '''
    head = {}
    head['User-Agent'] = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36'
    '''    
    data = {}
    data['i'] = content
    data['to'] = 'AUTO'
    data['smartresult'] = 'dict'
    data['client'] = 'fanyideskweb'
    data['salt'] = '1514268236312'
    data['sign'] = 'ce78c4d7e22e3963b41df1211e6d27aa'
    data['doctype'] = 'json'
    data['version'] = '2.1'
    data['keyfrom'] = 'fanyi.web'
    data['action'] = 'FY_BY_CLICKBUTTION'
    data['typoResult'] = 'false'
    data = urllib.parse.urlencode(data).encode('utf-8')

    req = urllib.request.Request(url,data)
    req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36')

    response = urllib.request.urlopen(req)
    html = response.read().decode('utf-8')
    target = json.loads(html)

    print("翻译结果：%s.\n" % (target['translateResult'][0][0]['tgt']))
    #time.sleep(0.1)
