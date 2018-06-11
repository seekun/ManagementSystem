import requests
from urllib.parse import urlencode
from requests.exceptions import ConnectionError
import re
from pyquery import PyQuery as pq


base_url='http://weixin.sogou.com/weixin?'
headers = {
    'Cookie':'SUV=00C55545DCB4387A5AD9A39087E11754; ABTEST=0|1524636483|v1; IPLOC=CN3401; SUID=3438B4DC2930990A000000005AE01B43; SUID=3438B4DC2320940A000000005AE01B43; weixinIndexVisited=1; sct=1; SNUID=84880473B0B5DA09A840F762B0F7EE3C; JSESSIONID=aaa6UlBuLP_lGd70FZ2lw; ppinf=5|1524636650|1525846250|dHJ1c3Q6MToxfGNsaWVudGlkOjQ6MjAxN3x1bmlxbmFtZTo2Olp1aVllZXxjcnQ6MTA6MTUyNDYzNjY1MHxyZWZuaWNrOjY6WnVpWWVlfHVzZXJpZDo0NDpvOXQybHVDYVBvYmZYbUd5V2VGdk9FVkxQZnVvQHdlaXhpbi5zb2h1LmNvbXw; pprdig=KzQ1T-E45-LHX-4N09uC_rbVPBSj-q0xZLGk33JKAfzE6t8ebxR2SKJvLMqg1NtUciAWy8xrgaVIf5LQgevAmxLw4G2O5M-ngMtSA4rApxqL9_LtQ-4kabDgUqbyok3iCxuhZ_nhlZyCgP0LuNg3jjcFOqqUUzRfqw4L8X7_3ug; sgid=19-34710031-AVrgGibpHT847FPMKQiaGicurw; ppmdig=15246366510000008b29ec374dbcaa8855b04f6def6f4ec0',
    'Host':'weixin.sogou.com',
    'Upgrade-Insecure-Requests':'1',
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
}
keyword = '风景'
proxy_pool_url = 'http://127.0.0.1:5000/get'
proxy = None
max_count = 5






def get_proxy():
    try:
        response = requests.get(proxy_pool_url)
        if response.status_code == 200:
            return response.text
        return None
    except ConnectionError:
        return None


def get_html(url,count=1):
    global proxy
    print("Crawling",url)
    print("Trying Count",count)
    if count >= max_count:
        print('Tried Too Many Counts')
        return None
    try:
        if proxy:
            proxies = {
                'http': 'http://' + proxy
            }
            response = requests.get(url, allow_redirects=False, headers=headers,proxies=proxies)
        else:
            response = requests.get(url, allow_redirects=False, headers=headers)
            if response.status_code == 200:
                return response.content.decode("utf-8")
            if response.status_code == 302:
                # Need Proxy
                print(302)
                proxy = get_proxy()
                if proxy:
                    print("Using the Proxy",proxy)
                    return get_html(url)
                else:
                    print("Get Proxy Failed")
                    return None
    except ConnectionError as e:
        print('Error Occurred', e.args)
        proxy = get_proxy()
        count +=1
        return get_html(url,count)



def get_index(keyword, page):
    data = {
        'query': keyword,
        'type': 2,
        'page': page
    }
    queries = urlencode(data) #转化为get请求参数
    url = base_url + queries
    html = get_html(url)
    return html

def parse_index(html):
    doc = pq(html)
    items = doc('.news-box .news-list li .txt-box h3 a ').items()
    for item in items:
        yield item.attr('href')

def get_detail(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        return None
    except ConnectionError:
        return None

def parse_detail(html):
    doc = pq(html)
    title = doc('.rich_media_title').text()
    content = doc('.rich_media_content').text()
    date = doc('#post-date').text()
    nickname = doc('#js_profile_qrcode > div > strong').text()
    wechat = doc('#js_profile_qrcode > div > p:nth-child(3) > span').text()
    return {
        'title': title,
        'content': content,
        'date': date,
        'nickname': nickname,
        'wechat': wechat
    }


def main():
    html = get_index(keyword, 1)
    if html:
        article_urls = parse_index(html)
        for article_url in article_urls:
            article_html = get_detail(article_url)
            if article_html:
                article_data = parse_detail(article_html)
                print(article_data)

if __name__ == '__main__':
    main()