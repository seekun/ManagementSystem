from django.db import models
from django.contrib.auth.models import AbstractUser
from jsonfield import JSONField
from prettyjson import PrettyJSONWidget
# from jsonfield import JSONField
from jsoneditor.forms import JSONEditor
# from jsoneditor.fields.django_json_field import JSONField

class User(AbstractUser):
    user_number = models.CharField('工号', max_length=20, blank=True)
    chinese_name = models.CharField('中文名', max_length=20, blank=True)
    english_name = models.CharField('论文署名一', null=True, blank=True, default=None, max_length=20)
    english_name2 = models.CharField('论文署名二', null=True, blank=True, default=None, max_length=20)
    english_name3 = models.CharField('论文署名三', null=True, blank=True, default=None, max_length=20,)
    english_name4 = models.CharField('论文署名四', null=True, blank=True, default=None, max_length=20,)
    # list字段,可以有多个english_name
    department = models.CharField('所在院系名称', max_length=20, blank=True)

    class Meta(AbstractUser.Meta):
        pass


class TestModel(models.Model):
    my_field = JSONField()
