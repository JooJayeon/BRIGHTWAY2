# Generated by Django 2.2.1 on 2019-06-07 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BrightWay', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CS',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('x', models.FloatField()),
                ('y', models.FloatField()),
            ],
        ),
        migrations.DeleteModel(
            name='ConvenienceShop',
        ),
    ]