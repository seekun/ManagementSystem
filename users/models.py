from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    user_number = models.CharField('工号', max_length=20, blank=True)
    chinese_name = models.CharField('中文名', max_length=20, blank=True)
    english_name = models.CharField('论文署名一', null=True, blank=True, default=None, max_length=20)
    english_name2 = models.CharField('论文署名二', null=True, blank=True, default=None, max_length=20)
    english_name3 = models.CharField('论文署名三', null=True, blank=True, default=None, max_length=20, )
    english_name4 = models.CharField('论文署名四', null=True, blank=True, default=None, max_length=20, )
    # list字段,可以有多个english_name
    department_list = (
        ('math', '数学科学学院'),
        ('physical', '物理与材料科学学院'),
        ('chemistry', '化学化工学院'),
        ('computer', '计算机科学与技术学院'),
        ('electric', '电子信息工程学院'),
        ('life', '生命科学学院'),
        ('book', '文学院'),
        ('history', '历史系'),
        ('philosophy', '哲学系'),
        ('news', '新闻传播学院'),
        ('economy', '经济学院'),
        ('business', '商学院'),
        ('foreign', '外语学院'),
        ('logic', '法学院'),
        ('manage', '管理学院'),
        ('society', '社会与政治学院'),
        ('art', '艺术学院'),
        ('environment', '资源与环境工程学院'),
        ('automate', '电气工程与自动化学院'),
        ('wengdian', '文典学院'),

    )
    department = models.CharField('所在院系名称', max_length=20, blank=True, choices=department_list)

    class Meta(AbstractUser.Meta):
        pass
