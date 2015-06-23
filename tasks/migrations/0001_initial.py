# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CurrentTask',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task', models.CharField(max_length=255)),
                ('frequency', models.CharField(choices=[(b'One Time', b'One Time'), (b'Weekly', b'Weekly'), (b'Monthly', b'Monthly')], default=b'One Time', max_length=10)),
                ('description', models.CharField(max_length=600)),
            ],
        ),
        migrations.CreateModel(
            name='TaskType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_due', models.DateTimeField(verbose_name=b'date due')),
                ('person_in_charge', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('type', models.ForeignKey(to='tasks.CurrentTask')),
            ],
        ),
    ]
