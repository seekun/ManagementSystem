import requests
from requests.exceptions import *
from urllib.parse import urlencode
from pyquery import PyQuery as pq
import json
import http.client
import re
import pymongo
import urllib3

client = pymongo.MongoClient('localhost')
db = client['webofscience']
#proxy_pool_url = 'http://127.0.0.1:5000/get'
max_count = 20 #代理尝试最大次数
max_page = 0 #需要爬取的页数 一页十篇
proxy = None
base_url = 'http://apps.webofknowledge.com/summary.do?'
qid = 5000 #默认为5000
sid = '' #默认为空
headers = {
    'Cookie': 'AUTO_LOGIN="ed2497ff87d7d493c4c7211ace5480175a75695965654368696e6140476d61696c2e636f6d"; SID="8FhgYPACqoFqlzFl7fo"; CUSTOMER="Anhui University"; E_GROUP_NAME="Anhui University"; ak_bmsc=34B7A76323A04820EF0408E40ACB552BB81A5BC50A1A00005053F65A85A8896E~pl0D3KtxnpH3MubLOChH4Ofc2F5qan1uYj4vD+Es406B0jwjel9OYBJrJNW/cXfYxAtmqNKjt06f/AZEUyyCM/MdLoF9p40LtQLASPFhMmMjTKuRU49a/4r5yvVLyMDSbNU4JZb+VHNrKoVk9OfYz1YcSZKUJoM7HMxpIZOBR8KmNF7g+zwdhw+lZAjYRkU+FmXWuiulv4QVScOqg1+wluWN2V0SSOA9E15zY4cLeK+iOwR5pzyk6SVbhN01AHaV7h; JSESSIONID=A6FB5AFA1867C8FEE3E9ADFD647DA950; bm_sv=1B2A7687195CED6E3D793AE198D9E532~tKz6JZE822c/ZxUjR8/Tl/FawxAdO7Px6R6vurILo9fHr55IudJqFfi98xpi2bTbu8akIpymQpO25ixMGJy1DA4VxvC3TBBdOxdkM/HskYQQ+GKW/PPAGYsd5AoR2OzDw4FRWEADUJZO9D9HDMwZ2GTFajNrplUvcB43cSPbC+4=',
    'Host': 'apps.webofknowledge.com',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
}


def get_sid():
    global sid
    try:
        sid_url = 'http://www.webofknowledge.com/'
        sid_url_response = requests.get(sid_url)
        if sid_url_response.status_code == 200:
            sid = re.findall(r'SID=\w+&', sid_url_response.url)[0].replace('SID=', '').replace('&', '')
            print("获取sid成功!sid=",sid)
        else:
            print("Get Sid Failed!")
            return None
    except ConnectionError:
        print("获取SID时连接错误，重试中...")
        get_sid()

def parse_page(page_str):
    page_str_parse = page_str.replace(',','')
    return int(page_str_parse)

def get_qid():
    global sid,qid,max_page
    form_data = {
        'fieldCount': 1,
        'action': 'search',
        'product': 'UA',
        'search_mode': 'GeneralSearch',
        'SID': sid,
        'max_field_count': 25,
        'max_field_notice': '',  # 注意: 无法添加另一字段。
        'input_invalid_notice': '',  # 检索错误: 请输入检索词。
        'exp_notice': '',  # 检索错误: 专利检索词可在多个家族中找到
        'input_invalid_notice_limits': '',  # <br/>注: 滚动框中显示的字段必须至少与一个其他检索字段相组配。
        'sa_params': 'UA||6CJReJ5m9lwBBxjs8t8|http://apps.webofknowledge.com|',
        'formUpdated': 'true',
        'value(input1)': 'Anhui Univ',
        'value(select1)': 'AD',
        'value(hidInput1)': '',
        'limitStatus': 'collapsed',
        'ss_lemmatization': 'On',
        'ss_spellchecking': 'Suggest',
        'SinceLastVisit_UTC': '',
        'SinceLastVisit_DATE': '',
        'period': 'Range Selection',
        'range': 'ALL',
        'startYear': '1950',
        'endYear': '2018',
        'update_back2search_link_param': 'yes',
        'ssStatus': 'display:none',
        'ss_showsuggestions': 'ON',
        'ss_query_language': 'auto',
        'ss_numDefaultGeneralSearchFields': 1,
        'rs_sort_by': 'PY.D;LD.D;SO.A;VL.D;PG.A;AU.A'
    }
    try:
        qid_url = 'http://apps.webofknowledge.com/UA_GeneralSearch.do'
        qid_session = requests.Session()
        qid_response = qid_session.post(qid_url, data=form_data)
        if qid_response.status_code == 200:
            qid_response.encoding = qid_response.apparent_encoding
            qid_doc = pq(qid_response.text)
            qid_items = qid_doc('.l-body .l-wrapper .l-wrapper-row .l-column-sidebar .refineSideBarCol').items()
            for qid_item in qid_items:
                qid_url = qid_item.attr('url')
            qid = re.findall(r'qid=\w+&', qid_url)[0].replace('qid=', '').replace('&', '')
            print("获取qid成功!,qid=", qid)
            max_page_str = qid_doc('#pageCount\.bottom').text()
            max_page = parse_page(max_page_str)
            print("获取max_page成功!,max_page=", max_page)
        else:
            print("Get qid failde!")
            return None
    except ConnectionError:
        print("获取QID时连接错误，重试中...")
        get_qid()



def get_proxy():
    try:
        response = requests.get(proxy_pool_url)
        if response.status_code == 200:
            return response.text
        return None
    except ConnectionError:
        return None

def get_html(url,page):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        else:
            print("Error Ourred!")
            return None
    except RequestException:
        print("连接错误4")
        handle_error1(page)
    except ConnectionError:
        print("连接错误5")
        handle_error1(page)
    except http.client.IncompleteRead:
        print("连接错误6")
        handle_error1(page)
    except requests.exceptions.ChunkedEncodingError:
        print("连接错误7")
        handle_error1(page)
    except urllib3.exceptions.NewConnectionError:
        print("连接错误8")
        handle_error1(page)
    except urllib3.exceptions.MaxRetryError:
        print("连接错误9")
        handle_error1(page)
    except requests.exceptions.ConnectionError:
        print("连接错误10")
        handle_error1(page)
    except TimeoutError:
        print("连接错误10")
        handle_error1(page)
    except urllib3.exceptions.NewConnectionError:
        print("连接错误11")
        handle_error1(page)

def get_index(page):
    global sid, qid
    data = {
        'product': 'UA',
        'colName': '',
        'qid': qid,
        'SID': sid,
        'search_mode': 'GeneralSearch',
        'formValue(summary_mode)': 'GeneralSearch',
        'update_back2search_link_param': 'yes',
        'page': page
    }
    queries = urlencode(data)
    url = base_url + queries
    print(url)
    html = get_html(url,page)
    return html

def parse_index(html):
    doc = pq(html)
    items = doc(' .search-results .search-results-content div div a').items()
    for item in items:
        yield item.attr('href')

def get_detail(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        else:
            print("连接错误1")
    except ConnectionError:
        print("连接错误2")
        handle_response = handle_error2(url)
        return handle_response.text
    except TimeoutError:
        print("连接错误3")
        handle_response = handle_error2(url)
        return handle_response.text

def parse_detail(html):
    doc = pq(html)
    author = '',
    title = '',
    periodical = '',
    year = '',
    volume = '',
    stage = '',
    leaf = '',
    dol = '',
    authors = doc('body > div.EPAMdiv.main-container > div.NEWfullRecord > form:nth-child(1) > input[type="hidden"]:nth-child(4)').items()
    for author in authors:
        author = author.attr('value')
    titles = doc('body > div.EPAMdiv.main-container > div.NEWfullRecord > form:nth-child(1) > input[type="hidden"]:nth-child(11)').items()
    for title in titles:
        title = title.attr('value')
    periodicals = doc('body > div.EPAMdiv.main-container > div.NEWfullRecord > form:nth-child(1) > input[type="hidden"]:nth-child(9)').items()
    for periodical in periodicals:
        periodical = periodical.attr('value')
    years = doc('body > div.EPAMdiv.main-container > div.NEWfullRecord > form:nth-child(1) > input[type="hidden"]:nth-child(8)').items()
    for year in years:
        year = year.attr('value')
    volumes = doc('body > div.EPAMdiv.main-container > div.NEWfullRecord > form:nth-child(1) > input[type="hidden"]:nth-child(6)').items()
    for volume in volumes:
        volume = volume.attr('value')
    stages = doc('body > div.EPAMdiv.main-container > div.NEWfullRecord > form:nth-child(1) > input[type="hidden"]:nth-child(7)').items()
    for stage in stages:
        stage = stage.attr('value')
    leafs = doc('body > div.EPAMdiv.main-container > div.NEWfullRecord > form:nth-child(1) > input[type="hidden"]:nth-child(10)').items()
    for leaf in leafs:
        leaf = leaf.attr('value')
    dols = doc('body > div.EPAMdiv.main-container > div.NEWfullRecord > form:nth-child(1) > input[type="hidden"]:nth-child(5)').items()
    for dol in dols:
        dol = dol.attr('value')
    dol_catalog = '',
    dol_1 = doc('.JCR_Category_table td:nth-child(1)').text()
    dol_2 = doc('.JCR_Category_table td:nth-child(2)').text()
    dol_3 = doc('.JCR_Category_table td:nth-child(3)').text()
    dol_catalog = dol_1 + " " + dol_2 + " " + dol_3
    address = ''
    for i in range(1, 10):
        ad = doc('.l-column-content tr:nth-child(' + str(i) + ') .fr_address_row2 a').text()
        if ad:
            address += ad + ' '
    return {
        'author': author,
        'title': title,
        'periodical': periodical,
        'year': year,
        'volume': volume,
        'stage': stage,
        'leaf': leaf,
        'dol': dol,
        'dol_catalog': dol_catalog,
        'address': address
    }

def save_to_mongo(data, page ,count):
    if db['articles'].update({'title': data['title']}, {'$set': data}, True):
        print('Saved page%d_article%d to Mongo'%(page, count))
    else:
        print('Saved page%d_article%d to Mongo Failed'%(page, count))


def save_to_local(content,page,count):
    with open("result_page%d_article%d.txt"%(page,count), 'a', encoding='utf-8') as f:
        f.write(json.dumps(content, ensure_ascii=False) + '\n')
        print("save result_page%d_article%d.txt successfully"%(page,count))
        f.close()



def main(page):
    article_count = 0
    html = get_index(page)
    if html:
        article_urls = parse_index(html)
        for article_url in article_urls:
            article_count += 1
            article_html = get_detail("http://apps.webofknowledge.com"+article_url)
            if article_html:
                article_data = parse_detail(article_html)
                save_to_mongo(article_data, page, article_count)

def handle_error1(page):
    get_sid()
    get_qid()
    get_index(page)
    print("handle the error1 completely!")

def handle_error2(url):
    global sid, qid
    get_sid()
    get_qid()
    error_doc = re.findall(r'doc=\w+', url)[0].replace('doc=', '')
    error_page = re.findall(r'page=\w+&', url)[0].replace('page=', '').replace('&', '')
    error_base_url = 'http://apps.webofknowledge.com/full_record.do?'
    data = {
        'product': 'UA',
        'search_mode': 'GeneralSearch',
        'qid': qid,
        'SID': sid,
        'page': error_page,
        'doc': error_doc
    }
    error_queries = urlencode(data)
    new_url = error_base_url + error_queries
    response = requests.get(new_url)
    if response.status_code == 200:
        return response
    else:
        print("handle the error2 Failed!")
    print("handle the error2 completely!")

if __name__ == '__main__':
    get_sid()
    get_qid()
    for page in range(1, max_page):
        main(page)