# Generated by Django 4.2.3 on 2023-07-15 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profriends',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='pics')),
                ('name', models.CharField(max_length=100)),
                ('desc', models.CharField(max_length=100)),
                ('acres', models.CharField(max_length=100)),
                ('dest', models.CharField(max_length=100)),
            ],
        ),
    ]
