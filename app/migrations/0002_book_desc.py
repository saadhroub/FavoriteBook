# Generated by Django 2.2.4 on 2022-04-09 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='desc',
            field=models.TextField(default='Nice'),
            preserve_default=False,
        ),
    ]
