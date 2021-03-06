# Generated by Django 2.1 on 2019-06-19 16:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0006_auto_20190619_1653'),
    ]

    operations = [
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice_text', models.CharField(max_length=200)),
                ('votes', models.IntegerField(default=0)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='choice', to='testapp.Quiz1')),
            ],
        ),
        migrations.RemoveField(
            model_name='choice1',
            name='question',
        ),
        migrations.DeleteModel(
            name='Choice1',
        ),
    ]
