# Generated by Django 2.1.3 on 2018-11-13 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventtime',
            name='disc',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='eventtime',
            name='title',
            field=models.CharField(default=1, max_length=40),
            preserve_default=False,
        ),
    ]
