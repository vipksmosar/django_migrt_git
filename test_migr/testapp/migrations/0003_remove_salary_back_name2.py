# Generated by Django 3.1.4 on 2020-12-04 11:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0002_salary_back_name2'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='salary',
            name='back_name2',
        ),
    ]
