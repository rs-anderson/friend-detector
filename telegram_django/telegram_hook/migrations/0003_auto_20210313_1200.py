# Generated by Django 3.1.7 on 2021-03-13 12:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('telegram_hook', '0002_auto_20210313_1046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stagedperson',
            name='person',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='telegram_hook.person'),
        ),
    ]
