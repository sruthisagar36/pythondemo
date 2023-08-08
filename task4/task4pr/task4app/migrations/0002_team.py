# Generated by Django 4.2.2 on 2023-07-10 04:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task4app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('names', models.CharField(max_length=250)),
                ('imgs', models.ImageField(upload_to='pics')),
                ('descp', models.TextField()),
            ],
        ),
    ]
