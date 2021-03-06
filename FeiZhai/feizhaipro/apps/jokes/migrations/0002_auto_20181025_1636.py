# Generated by Django 2.0.6 on 2018-10-25 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jokes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='joke',
            name='jokecontent',
            field=models.CharField(max_length=5000, verbose_name='笑话内容'),
        ),
        migrations.AlterField(
            model_name='joke',
            name='jokeimg',
            field=models.ImageField(null=True, upload_to='jokeimg', verbose_name='笑话图片'),
        ),
    ]
