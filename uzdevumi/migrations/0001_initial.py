# Generated by Django 3.2.8 on 2021-11-21 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Visit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('visitor', models.CharField(max_length=100)),
                ('reason', models.CharField(max_length=140)),
                ('date_time', models.DateTimeField()),
            ],
        ),
    ]
