# Generated by Django 2.2 on 2020-03-22 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20200322_1026'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='count',
            field=models.IntegerField(),
        ),
    ]
