# Generated by Django 3.2.7 on 2021-09-04 22:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biblioteca', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='bookPhoto',
            field=models.ImageField(blank=True, null=True, upload_to='../dbimages/'),
        ),
    ]