# Generated by Django 2.0.6 on 2018-10-30 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0003_auto_20181030_1124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goodsdetail',
            name='goodscon',
            field=models.TextField(blank=True, verbose_name='商品简介'),
        ),
    ]
