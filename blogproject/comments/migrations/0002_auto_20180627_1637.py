# Generated by Django 2.0.4 on 2018-06-27 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='url',
            field=models.URLField(),
        ),
    ]
