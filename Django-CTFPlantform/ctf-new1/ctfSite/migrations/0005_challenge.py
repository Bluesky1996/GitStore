# Generated by Django 2.0 on 2017-11-05 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ctfSite', '0004_notice'),
    ]

    operations = [
        migrations.CreateModel(
            name='challenge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('info', models.CharField(max_length=500)),
                ('flag', models.CharField(max_length=50)),
                ('type', models.CharField(max_length=10)),
            ],
        ),
    ]