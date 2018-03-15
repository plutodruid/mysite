# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-02-06 09:36
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('article', '0006_auto_20180127_1732'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='articlepost',
            options={'ordering': ('-updated',)},
        ),
        migrations.AddField(
            model_name='articlepost',
            name='users_like',
            field=models.ManyToManyField(blank=True, related_name='articles_like', to=settings.AUTH_USER_MODEL),
        ),
    ]
