# Generated by Django 2.0 on 2017-11-05 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ctfSite', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='num2',
            field=models.CharField(default=123, max_length=50),
        ),
        migrations.AddField(
            model_name='team',
            name='qq2',
            field=models.CharField(default=123, max_length=50),
        ),
        migrations.AddField(
            model_name='team',
            name='st2',
            field=models.CharField(default='abc', max_length=50),
        ),
        migrations.AddField(
            model_name='team',
            name='stnum2',
            field=models.CharField(default=123, max_length=50),
        ),
    ]
