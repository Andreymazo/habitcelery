# Generated by Django 4.1.6 on 2023-03-15 00:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mailing', '0005_delete_mssg'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Client',
        ),
    ]