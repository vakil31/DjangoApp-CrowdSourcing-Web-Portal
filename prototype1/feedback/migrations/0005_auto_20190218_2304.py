# Generated by Django 2.1.5 on 2019-02-18 23:04

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0004_auto_20190206_1805'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='videourl',
            managers=[
                ('urlobj', django.db.models.manager.Manager()),
            ],
        ),
    ]
