# Generated by Django 3.2.7 on 2021-09-23 09:55

from django.db import migrations, models
import django.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('biblioteca', '0005_alter_books_bookphoto'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='link',
            field=models.CharField(default=django.db.models.fields.NullBooleanField, max_length=255),
        ),
    ]
