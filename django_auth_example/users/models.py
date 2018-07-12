from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.postgres.fields import JSONField
import json


class User(AbstractUser):
    user_number = models.CharField('工号', max_length=20, blank=True)
    chinese_name = models.CharField('中文名', max_length=20, blank=True)
    english_name = JSONField(blank=True, null=True)
    # list字段,可以有多个english_name
    department = models.CharField('所在院系名称', max_length=20, blank=True)

    class Meta(AbstractUser.Meta):
        pass
