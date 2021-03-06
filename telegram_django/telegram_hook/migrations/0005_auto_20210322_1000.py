# Generated by Django 3.1.7 on 2021-03-22 10:00

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('telegram_hook', '0004_delete_stagedperson'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='person',
            options={'ordering': ['id'], 'verbose_name': 'Person', 'verbose_name_plural': 'People'},
        ),
        migrations.AddField(
            model_name='person',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
