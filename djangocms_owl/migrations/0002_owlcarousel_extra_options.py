# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('djangocms_owl', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='owlcarousel',
            name='extra_options',
            field=jsonfield.fields.JSONField(default=dict, verbose_name='JSON options', blank=True),
            preserve_default=True,
        ),
    ]
