# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0013_auto_20150704_1500'),
    ]

    operations = [
        migrations.CreateModel(
            name='OwlCarousel',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('pagination', models.BooleanField(default=False, help_text='Show pagination. (dot dot dot)')),
                ('pagination_numbers', models.BooleanField(default=False, help_text='Show numbers inside pagination buttons')),
                ('navigation', models.BooleanField(default=False, help_text='Display "next" and "prev" buttons.')),
                ('autoplay', models.BooleanField(default=False, help_text='Slides cycle automatically every 5 seconds')),
                ('stop_on_hover', models.BooleanField(default=False, help_text='Stop autoplay on mouse hover')),
                ('items', models.PositiveSmallIntegerField(default=1, help_text='maximum amount of items displayed at a time')),
                ('auto_height', models.BooleanField(default=False, help_text='Add height to owl-wrapper-outer so you can use diffrent heights on slides.')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
