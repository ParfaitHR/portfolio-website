# Generated by Django 3.1.4 on 2020-12-17 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_name', models.CharField(max_length=30, null=True)),
                ('description', models.CharField(max_length=256, null=True)),
                ('date', models.DateField(null=True)),
                ('time', models.TimeField(null=True)),
                ('last_date', models.DateField(null=True)),
                ('contact', models.CharField(max_length=30)),
            ],
        ),
    ]
