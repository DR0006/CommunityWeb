# Generated by Django 4.2.6 on 2023-11-06 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_demo', '0002_alter_topiccomment_body'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topiccomment',
            name='body',
            field=models.TextField(blank=True, default='', max_length=20000, verbose_name='内容'),
        ),
    ]
