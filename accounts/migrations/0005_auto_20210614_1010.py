# Generated by Django 3.1.7 on 2021-06-14 04:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20210613_2116'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='desc',
            new_name='description',
        ),
    ]
