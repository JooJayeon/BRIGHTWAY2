# Generated by Django 2.2.2 on 2019-06-10 21:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BrightWay', '0009_auto_20190611_0630'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dong',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('distinct', models.TextField()),
                ('x', models.FloatField()),
                ('y', models.FloatField()),
            ],
        ),
    ]
