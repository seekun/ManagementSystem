from pyquery import PyQuery as pq
import requests
from html import htmls



doc = pq(htmls)
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
print('Title=', Title)

Periodicals = doc('body > div.EPAMdiv.main-container > div.NEWfullRecord > form:nth-child(1) > input[type="hidden"]:nth-child(9)').items()
for Periodical in Periodicals:
    Periodical = Periodical.attr('value')
print('Periodical=', Periodical)

Years = doc('body > div.EPAMdiv.main-container > div.NEWfullRecord > form:nth-child(1) > input[type="hidden"]:nth-child(8)').items()
for Year in Years:
    Year = Year.attr('value')
print('Year=', Year)

Volumes = doc('body > div.EPAMdiv.main-container > div.NEWfullRecord > form:nth-child(1) > input[type="hidden"]:nth-child(6)').items()
for Volume in Volumes:
    Volume = Volume.attr('value')
print('Volume=', Volume)

Stages = doc('body > div.EPAMdiv.main-container > div.NEWfullRecord > form:nth-child(1) > input[type="hidden"]:nth-child(7)').items()
for Stage in Stages:
    Stage = Stage.attr('value')
print('Stage=', Stage)

Leafs = doc('body > div.EPAMdiv.main-container > div.NEWfullRecord > form:nth-child(1) > input[type="hidden"]:nth-child(10)').items()
for Leaf in Leafs:
    Leaf = Leaf.attr('value')
print('Leaf=', Leaf)

DOIs = doc('body > div.EPAMdiv.main-container > div.NEWfullRecord > form:nth-child(1) > input[type="hidden"]:nth-child(5)').items()
for DOI in DOIs:
    DOI = DOI.attr('value')
print('dol=', DOI)




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
print("JCR_categorys=", JCR_categorys)

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
print("JCR_sorts=", JCR_sorts)

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
print("JCR_partitions=", JCR_partitions)

Authors = []
i=0
while True:
    i = i + 2
    Author = ''
    Author = doc('.l-column-content .l-content div:nth-child(6) > p > a:nth-child(%d)'%i).text()
    if Author:
        Authors.append(Author)
    else:
        break
print("Authors=", Authors)

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
print("Authors_number=", Authors_number)

body = doc('.l-column-content .l-content div:nth-child(8) > p').text()
print(body)


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
print("Author_key_words=", Author_key_words)


Key_words_pluses = []
i=1
while True:
    i = i + 1
    Key_words_plus = ''
    Key_words_plus = doc('.l-column-content .l-content div:nth-child(9) > p:nth-child(3) > a:nth-child(%d)'%i).text()
    if Key_words_plus:
        Key_words_pluses.append(Key_words_plus)
    else:
        break
print("Key_words_pluses=", Key_words_pluses)

#通讯作者
communication_author = doc('.l-column-content .l-content div:nth-child(10) > p:nth-child(2)').text().replace('Reprint Address:', '')
print("communication_author=", communication_author)


#通讯作者地址
communication_author_address = doc('.l-column-content .l-content div:nth-child(10) > table:nth-child(3) .fr_address_row2').text().replace('Organization-Enhanced Name(s)', '').replace('Anhui University', '').replace('\n', '')
print("communication_author_address=", communication_author_address)


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
print("addresses=", addresses)





email = []
email = doc(' .l-column-content div:nth-child(10) p:nth-child(8) a:nth-child(2)').text()
print("email=", email)

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
print("Fund_funded_institutions=", Fund_funded_institutionses)

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
print("Fund_funded_institutions_authorization_numbers=", Fund_funded_institutions_authorization_numbers)

Fund_information = doc('#show_fund_blurb > p').text() #基金资助信息
print('Fund_information=', Fund_information)

Influence_factor = doc(' .Impact_Factor_table td:nth-child(1)').text() #对应年份影响因子
print('Influence_factor=', Influence_factor)

Influence_factors = doc(' .Impact_Factor_table td:nth-child(2)').text() #近几年影响因子
print('Influence_factors=', Influence_factors)

Influence_factors_year = doc(' .Impact_Factor_table th:nth-child(1)').text() #对应年份影响因子
print('Influence_factors_year=', Influence_factors_year)

Influence_factors_years = doc(' .Impact_Factor_table th:nth-child(2)').text() #对应年份影响因子
print('Influence_factors_years=', Influence_factors_years)

ISSN = doc('#show_journal_overlay_7 > p.FR_field.sameLine > value:nth-child(2)').text()
print('ISSN=', ISSN)

eISSN = doc('#show_journal_overlay_7 > p.FR_field.sameLine > value:nth-child(5)').text()
print('eISSN=', eISSN)


i=0
Research_fields = []#研究领域
while True:
    i = i + 2
    Research_field = ''
    Research_field = doc('#show_journal_overlay_7 > p:nth-child(5) > value:nth-child(%d)'%i).text()  # 基金资助机构
    if Research_field:
        Research_fields.append(Research_field)
    else:
        break
print("Research_fields=", Research_fields)

Collection_number = doc('#hidden_section > div:nth-child(1) > p:nth-child(3) > value').text()
print('Collection_number=', Collection_number)

IDS = doc('#hidden_section > div:nth-child(2) > p:nth-child(2) > value').text()
print('IDS=', IDS)

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
    '基金资助机构': Fund_funded_institutions,
    '授权号': Fund_funded_institutions_authorization_numbers,
    '基金资助信息': Fund_information,
    '指定年份影响因子': Influence_factor,
    '近年影响因子': Influence_factor,
    '指定年份': Influence_factors_year,
    '近年': Influence_factors_years,
    'ISSN': ISSN,
    'eISSN': eISSN,
    '研究方向': Research_fields,
    '入藏号': Collection_number,
    'IDS号': IDS
    }
print(s)