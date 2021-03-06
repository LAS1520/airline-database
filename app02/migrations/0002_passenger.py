# Generated by Django 3.2.3 on 2021-06-05 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app02', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Passenger',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('idnum', models.CharField(max_length=20, unique=True)),
                ('telnum', models.CharField(max_length=40)),
                ('user', models.ManyToManyField(to='app02.User')),
            ],
        ),
    ]
