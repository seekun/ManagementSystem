from django.contrib import admin
from .models import User, TestModel
from django.contrib.postgres import fields
from django_json_widget.widgets import JSONEditorWidget
from prettyjson import PrettyJSONWidget

admin.site.register(User)
admin.site.register(TestModel)


#
# class User(admin.ModelAdmin):
#     formfield_overrides = {
#         fields.JSONField: {'widget': JSONEditorWidget},
#     }

#
# from jsonfield import JSONField
# from jsoneditor.forms import JSONEditor
#
#
# class MyAdmin(admin.ModelAdmin):
#     formfield_overrides = {
#         JSONField: {'widget': JSONEditor},
#     }


# class YourModelAdmin(admin.ModelAdmin):
#     formfield_overrides = {
#         fields.JSONField: {'widget': JSONEditorWidget},
#     }

#
# class JsonAdmin(admin.ModelAdmin):
#     form = TestModel


from django.contrib.postgres.fields import JSONField


class JsonAdmin(admin.ModelAdmin):
    formfield_overrides = {
        JSONField: {'widget': PrettyJSONWidget}
    }
