# Generated by Django 2.0.5 on 2018-05-28 01:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_remove_user_nickname'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='user_number',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]