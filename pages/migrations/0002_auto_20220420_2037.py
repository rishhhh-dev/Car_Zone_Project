# Generated by Django 3.0.7 on 2022-04-20 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='photo',
            field=models.ImageField(upload_to='media/image/%Y/%m/%d/'),
        ),
    ]