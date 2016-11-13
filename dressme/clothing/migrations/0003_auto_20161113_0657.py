# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-13 06:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clothing', '0002_auto_20161112_2036'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stormchaser',
            name='zipcode',
        ),
        migrations.RemoveField(
            model_name='wardrobe',
            name='inLaundry',
        ),
        migrations.AddField(
            model_name='stormchaser',
            name='city',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AddField(
            model_name='stormchaser',
            name='state',
            field=models.CharField(blank=True, max_length=2),
        ),
        migrations.AddField(
            model_name='stormchaser',
            name='wardrobe',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='clothing.Wardrobe'),
        ),
        migrations.AddField(
            model_name='wardrobe',
            name='for_chilly',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='wardrobe',
            name='for_cold',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='wardrobe',
            name='for_hot',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='wardrobe',
            name='for_mild',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='wardrobe',
            name='for_warm',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='wardrobe',
            name='in_laundry',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='wardrobe',
            name='cloth_name',
            field=models.IntegerField(choices=[(1, 'T-SHIRT'), (2, 'POLO'), (3, 'BUTTONED_SHIRT'), (4, 'JEANS'), (5, 'SHORTS'), (6, 'SWEATS'), (7, 'COAT'), (8, 'HOODIE'), (9, 'SWEATER'), (10, 'EARMUFFS'), (11, 'SCARF'), (12, 'GLOVES')]),
        ),
    ]