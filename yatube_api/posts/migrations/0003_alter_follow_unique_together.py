# Generated by Django 3.2.16 on 2023-05-04 00:02

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0002_auto_20230504_0931'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='follow',
            unique_together={('user', 'following')},
        ),
    ]
