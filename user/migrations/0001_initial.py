# Generated by Django 4.1.1 on 2022-10-01 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('username', models.CharField(max_length=60)),
                ('dateBirth', models.DateField()),
                ('password', models.CharField(max_length=40)),
            ],
        ),
    ]
