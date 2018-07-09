from mongoengine import *
from mongoengine import connect

connect('paper', host='127.0.0.1', port=27017)


class ArtiInFo(Document):
    title = StringField('论文题目')
    address = StringField('作者地址')
    author = StringField('作者名单')
    dol = StringField('分区索引')
    dol_catalog = StringField('分区索引目录')
    leaf = StringField('页')
    periodical = StringField('发表期刊')
    stage = StringField('卷')
    volume = StringField('期')
    year = StringField('发表日期')
    checkout = BooleanField(default=True)

    meta = {
        'collection': 'articles'
    }
