# Generated by Django 3.1.7 on 2021-03-13 10:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('telegram_hook', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='person',
            options={'verbose_name': 'Person', 'verbose_name_plural': 'People'},
        ),
        migrations.CreateModel(
            name='StagedPerson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('person', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='telegram_hook.person')),
            ],
            options={
                'verbose_name': 'Staged Person',
                'verbose_name_plural': 'Staged Person',
            },
        ),
    ]