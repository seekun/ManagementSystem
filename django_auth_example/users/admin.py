from django.contrib import admin
from .models import User

from prettyjson import PrettyJSONWidget

admin.site.register(User)
