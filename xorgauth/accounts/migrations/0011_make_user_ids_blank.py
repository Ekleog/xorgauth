# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2017-12-27 22:18
from __future__ import unicode_literals

from django.db import migrations, models
import xorgauth.utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_make_roles_optional'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='axid',
            field=xorgauth.utils.fields.UnboundedCharField(blank=True, help_text='Identification in AX directory',
                                                           null=True, verbose_name='AX ID'),
        ),
        migrations.AlterField(
            model_name='user',
            name='grad_year',
            field=models.IntegerField(blank=True, help_text='Year of the graduation', null=True,
                                      verbose_name='graduation year'),
        ),
        migrations.AlterField(
            model_name='user',
            name='schoolid',
            field=xorgauth.utils.fields.UnboundedCharField(blank=True, help_text='Identification defined by the School',
                                                           null=True, unique=False, verbose_name='School ID'),
        ),
        migrations.AlterField(
            model_name='user',
            name='study_year',
            field=xorgauth.utils.fields.UnboundedCharField(
                blank=True,
                help_text="Kind and main year of the study ('X1829' means 'entered the school in 1829 "
                "but 'M2005' means 'graduated in 2005')", null=True, verbose_name='study year'),
        ),
    ]
