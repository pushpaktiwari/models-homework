# Generated by Django 2.0.1 on 2018-01-30 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CricketerNames',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('playerName', models.CharField(max_length=200)),
                ('playerRole', models.CharField(max_length=200)),
            ],
        ),
    ]
