# Generated by Django 3.0.5 on 2020-04-24 06:26

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('crawler', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sharedailyhistory',
            old_name='first',
            new_name='open',
        ),
    ]
