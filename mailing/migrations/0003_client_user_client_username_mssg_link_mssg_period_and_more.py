# Generated by Django 4.1.6 on 2023-03-14 21:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mailing', '0002_emails_mailinglog_alter_client_options_and_more'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='user',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='profile', to='users.user'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='client',
            name='username',
            field=models.CharField(default=1, max_length=150, unique=True, verbose_name='username'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mssg',
            name='link',
            field=models.ForeignKey(blank=True, default=1, max_length=100, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Какому клиенту относится'),
        ),
        migrations.AddField(
            model_name='mssg',
            name='period',
            field=models.TimeField(auto_now=True, choices=[(86400, 'день=86400'), (604800, 'неделя=604800'), (2419200, 'месяц=2419200')], max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='mssg',
            name='status',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='client',
            name='comment',
            field=models.TextField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='mssg',
            name='text',
            field=models.CharField(max_length=100, verbose_name='Текст сообщения'),
        ),
        migrations.AddField(
            model_name='emails',
            name='comment',
            field=models.ForeignKey(blank=True, default=1, max_length=100, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Какому клиенту относится'),
        ),
    ]
