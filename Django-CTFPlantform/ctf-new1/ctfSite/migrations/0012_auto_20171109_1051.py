# Generated by Django 2.0 on 2017-11-09 02:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ctfSite', '0011_auto_20171106_1947'),
    ]

    operations = [
        migrations.RenameField(
            model_name='challenge',
            old_name='title',
            new_name='category',
        ),
        migrations.RemoveField(
            model_name='challenge',
            name='info',
        ),
        migrations.RemoveField(
            model_name='challenge',
            name='point',
        ),
        migrations.RemoveField(
            model_name='challenge',
            name='type',
        ),
        migrations.AddField(
            model_name='challenge',
            name='description',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='challenge',
            name='name',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='challenge',
            name='value',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='challenge',
            name='flag',
            field=models.CharField(max_length=100),
        ),
    ]
