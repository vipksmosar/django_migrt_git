# Generated by Django 3.1.4 on 2020-12-04 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='salary',
            name='back_name2',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
