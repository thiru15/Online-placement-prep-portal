# Generated by Django 2.1 on 2019-06-19 11:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0005_auto_20190619_1645'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='choice2',
            name='question',
        ),
        migrations.DeleteModel(
            name='Choice2',
        ),
        migrations.DeleteModel(
            name='Quiz2',
        ),
    ]
