from mongoengine import *
from mongoengine import connect
connect('webofscience', host='127.0.0.1', port=27017)


class ArtiInFo(Document):
    title = StringField('论文题目')
    address = StringField('作者地址')
    author = StringField('作者名字')
    dol = StringField()
    dol_catalog = StringField()
    leaf = StringField()
    periodical = StringField()
    stage = StringField()
    volume = StringField()
    year = StringField('发表日期')

    meta = {
        'collection': 'articles'
    }