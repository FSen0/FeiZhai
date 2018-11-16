# Generated by Django 2.0.6 on 2018-10-29 03:54

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('news', '0003_auto_20181026_1509'),
    ]

    operations = [
        migrations.CreateModel(
            name='Relationartuser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('art', models.ForeignKey(on_delete=True, to='news.Article')),
                ('user', models.ForeignKey(on_delete=True, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '文章收藏',
                'verbose_name_plural': '文章收藏',
                'db_table': 'fz_artcollect',
            },
        ),
    ]
