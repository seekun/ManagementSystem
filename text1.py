from pyquery import PyQuery as pq
import requests

url = 'http://apps.webofknowledge.com/full_record.do?product=UA&search_mode=GeneralSearch&qid=1&SID=7DPszYGWhcrQUCMIm9Y&page=3&doc=29'
html = requests.get(url).text

doc = pq(html)
Author = '',
Title = '',
Periodical = '',
Year = '',
Volume = '',
Stage = '',
Leaf = '',
DOI = '',

Titles = doc('body > div.EPAMdiv.main-container > div.NEWfullRecord > form:nth-child(1) > input[type="hidden"]:nth-child(11)').items()
for Title in Titles:
    Title = Title.attr('value')


Periodicals = doc('body > div.EPAMdiv.main-container > div.NEWfullRecord > form:nth-child(1) > input[type="hidden"]:nth-child(9)').items()
for Periodical in Periodicals:
    Periodical = Periodical.attr('value')


Years = doc('body > div.EPAMdiv.main-container > div.NEWfullRecord > form:nth-child(1) > input[type="hidden"]:nth-child(8)').items()
for Year in Years:
    Year = Year.attr('value')


Volumes = doc('body > div.EPAMdiv.main-container > div.NEWfullRecord > form:nth-child(1) > input[type="hidden"]:nth-child(6)').items()
for Volume in Volumes:
    Volume = Volume.attr('value')


Stages = doc('body > div.EPAMdiv.main-container > div.NEWfullRecord > form:nth-child(1) > input[type="hidden"]:nth-child(7)').items()
for Stage in Stages:
    Stage = Stage.attr('value')


Leafs = doc('body > div.EPAMdiv.main-container > div.NEWfullRecord > form:nth-child(1) > input[type="hidden"]:nth-child(10)').items()
for Leaf in Leafs:
    Leaf = Leaf.attr('value')


DOIs = doc('body > div.EPAMdiv.main-container > div.NEWfullRecord > form:nth-child(1) > input[type="hidden"]:nth-child(5)').items()
for DOI in DOIs:
    DOI = DOI.attr('value')





JCR_categorys = [] #JCR类别
i=1
while True:
    i = i + 1
    JCR_category = ''
    JCR_category = doc('.JCR_Category_table  tr:nth-child(%d) td:nth-child(1)'%i).text()
    if JCR_category:
        JCR_categorys.append(JCR_category)
    else:
        break


JCR_sorts = [] #JCR类别中的排序
i=1
while True:
    i = i + 1
    JCR_sort = ''
    JCR_sort = doc('.JCR_Category_table  tr:nth-child(%d) td:nth-child(2)'%i).text()
    if JCR_sort:
        JCR_sorts.append(JCR_sort)
    else:
        break


JCR_partitions = [] #JCR分区
i=1
while True:
    i = i + 1
    JCR_partition = ''
    JCR_partition = doc('.JCR_Category_table  tr:nth-child(%d) td:nth-child(3)'%i).text()
    if JCR_partition:
        JCR_partitions.append(JCR_partition)
    else:
        break


Authors_number = []
i=1
while True:
    i = i + 2
    Author_number = ''
    Author_number = doc('.l-column-content .l-content div:nth-child(6) > p > sup:nth-child(%d) > b > a > b'%i).text()
    if Author_number:
        Authors_number.append(Author_number)
    else:
        break

if Authors_number:
    number = 6
else:
    number = 5
Authors = []
i=0
while True:
    i = i + 2
    Author = ''
    Author = doc('.l-column-content .l-content div:nth-child(%d) > p > a:nth-child(%d)'%(number, i)).text()
    if Author:
        Authors.append(Author)
    else:
        break





body = doc('.l-column-content .l-content div:nth-child(8) > p').text()



Author_key_words = []
i=1
while True:
    i = i + 1
    Author_key_word = ''
    Author_key_word = doc('.l-column-content .l-content div:nth-child(9) > p:nth-child(2) > a:nth-child(%d)'%i).text()
    if Author_key_word:
        Author_key_words.append(Author_key_word)
    else:
        break



Key_words_pluses = []
i=1
while True:
    i = i + 1
    Key_words_plus = ''
    Key_words_plus = doc('.l-column-content .l-content div:nth-child(9) > p:nth-child(2) > a:nth-child(%d)'%i).text()
    if Key_words_plus:
        Key_words_pluses.append(Key_words_plus)
    else:
        break


#通讯作者
communication_author = doc('.l-column-content .l-content div:nth-child(10) > p:nth-child(2)').text().replace('Reprint Address:', '')



#通讯作者地址
communication_author_address = doc('.l-column-content .l-content div:nth-child(10) > table:nth-child(3) .fr_address_row2').text().replace('Organization-Enhanced Name(s)', '').replace('Anhui University', '').replace('\n', '')



addresses = []
i=0
while True:
    i = i + 1
    address = ''
    address = doc('.l-column-content tr:nth-child(%d) .fr_address_row2 a'%i).text()
    if address:
        addresses.append(address)
    else:
        break

email = doc('.l-content div:nth-child(10) > p:nth-child(6)').text()


i=1
Fund_funded_institutionses =[]#基金资助机构
while True:
    i = i + 1
    Fund_funded_institutions = ''
    Fund_funded_institutions = doc('.l-column-content .l-content div:nth-child(11) tr:nth-child(%d) td:nth-child(1)'%i).text()
    if Fund_funded_institutions:
        Fund_funded_institutionses.append(Fund_funded_institutions)
    else:
        break


i=1
Fund_funded_institutions_authorization_numbers =[] #基金资助机构授权号
while True:
    i = i + 1
    Fund_funded_institutions_authorization_number = ''
    Fund_funded_institutions_authorization_number = doc('.l-column-content .l-content div:nth-child(11) tr:nth-child(%d) td:nth-child(2)'%i).text()  # 基金资助机构
    if Fund_funded_institutions_authorization_number:
        Fund_funded_institutions_authorization_numbers.append(Fund_funded_institutions_authorization_number)
    else:
        break


Fund_information = doc('#show_fund_blurb > p').text() #基金资助信息


Influence_factor = doc(' .Impact_Factor_table td:nth-child(1)').text() #对应年份影响因子


Influence_factors = doc(' .Impact_Factor_table td:nth-child(2)').text() #近几年影响因子


Influence_factors_year = doc(' .Impact_Factor_table th:nth-child(1)').text() #对应年份影响因子


Influence_factors_years = doc(' .Impact_Factor_table th:nth-child(2)').text() #对应年份影响因子


ISSN = doc('#hidden_section > div:nth-child(1) > p:nth-child(4) > value').text()


eISSN = doc('#hidden_section > div:nth-child(1) > p:nth-child(5) > value').text()




#研究领域
Research_field = doc('.l-column-content .l-content div:nth-child(14) > p:nth-child(2)').text()



Collection_number = doc('#hidden_section > div:nth-child(1) > p:nth-child(3) > value').text()


IDS = doc('#hidden_section > div:nth-child(2) > p:nth-child(2) > value').text()


s = {
    '作者': Authors,
    '作者对应地址': Authors_number,
    '论文名称': Title,
    '期刊': Periodical,
    '出版年': Year,
    '卷': Volume,
    '期': Stage,
    '页': Leaf,
    'DOI': DOI,
    'JCR® 类别': JCR_categorys,
    'JCR类别排序': JCR_sorts,
    'JCR 分区': JCR_partitions,
    '摘要': body,
    '作者关键词': Author_key_words,
    'KeyWords Plus': Key_words_pluses,
    '通讯作者': communication_author,
    '通讯作者地址': communication_author_address,
    '地址': addresses,
    'email': email,
    '基金资助机构': Fund_funded_institutionses,
    '授权号': Fund_funded_institutions_authorization_numbers,
    '基金资助信息': Fund_information,
    '指定年份影响因子': Influence_factor,
    '近年影响因子': Influence_factor,
    '指定年份': Influence_factors_year,
    '近年': Influence_factors_years,
    'ISSN': ISSN,
    'eISSN': eISSN,
    '研究方向': Research_field,
    '入藏号': Collection_number,
    'IDS号': IDS
    }
print(s)