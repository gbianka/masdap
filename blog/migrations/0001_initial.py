# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('puput', '0002_auto_20181213_0854'),
        ('maps', '0030_auto_20180414_2120'),
    ]

    operations = [
        migrations.CreateModel(
            name='MapEntryPage',
            fields=[
                ('entrypage_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='puput.EntryPage')),
                ('map', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='maps.Map')),
            ],
            options={
                'abstract': False,
            },
            bases=('puput.entrypage',),
        ),
    ]

