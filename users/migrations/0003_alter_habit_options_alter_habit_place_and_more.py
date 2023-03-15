# Generated by Django 4.1.6 on 2023-03-15 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_habit'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='habit',
            options={'permissions': [('set_is_published', 'Can publish habit')]},
        ),
        migrations.AlterField(
            model_name='habit',
            name='place',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='место'),
        ),
        migrations.AlterField(
            model_name='habit',
            name='useful',
            field=models.BooleanField(blank=True, default=True, null=True, verbose_name='полезная привычка или нет'),
        ),
    ]
