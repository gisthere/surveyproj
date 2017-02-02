# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questionnaire', '0003_auto_20170202_1758'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='language',
            field=models.CharField(default=b'en-us', max_length=2, verbose_name='Language', choices=[(b'en', b'English'), (b'ru', b'Russian')]),
        ),
    ]
