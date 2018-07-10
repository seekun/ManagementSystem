from mongoengine import *
from mongoengine import connect

connect('paper', host='127.0.0.1', port=27017)


class ArtiInFo(Document):
    authors = ListField()
    authors_number = ListField()
    title = StringField('论文标题')
    periodical = StringField('发表期刊')
    year = StringField('发表日期')
    volume = StringField('卷')
    stage = StringField('期')
    leaf = StringField('页')
    DOI = StringField('DOI')
    JCR_categories = ListField()
    JCR_sorts = ListField()
    JCR_partitions = ListField()
    body = StringField('摘要')
    author_key_words = ListField()
    Key_words_pluses = StringField('KeyWords Plus')
    KeyWords_Plus = StringField("KeyWords ")
    communication_author = StringField('通讯作者')
    communication_author_address = StringField('通讯作者地址')
    addresses = ListField()
    email = StringField('email')
    Fund_funded_institutions = StringField('基金资助机构')
    Fund_funded_institutions_authorization_numbers = ListField()
    Fund_information = StringField('基金资助信息')
    Influence_factor = StringField('指定年份影响因子')
    Influence_factors_year = StringField('指定年份')
    Influence_factors_years = StringField('近年')
    ISSN = StringField('ISSN')
    eISSN = StringField('eISSN')
    Research_fields = StringField('研究方向')
    Collection_number = StringField('入藏号')
    IDS = StringField('IDS')
    checkout = BooleanField(default=True)
    # 在括号里加的字段,当时不知道能不能加,加了之后也不知道起不起作用,当时完全是凭感觉加的,但是数据类型的字段修改为
    # ListField()时,如果还继续只加一个字段说明,与list的类型不符,所以报错了.
    # 报错后处理的方式不对, 一开始直接贴google,没找到解决方法;后来开始尝试读文档, 开始读Django文档,后来意识到报错的是mongoengine, 卡了很长时间,通过和mongoengine文档的对比,找到了不同之处
    # 最后发现了问题所在. 反复测试,尝试, 是找bug的好办法

    # belongs_to = Document.ManyToManyField(User)
    meta = {
        'collection': 'articles'
    }

