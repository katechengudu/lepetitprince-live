# Generated by Django 3.2.4 on 2021-06-18 05:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rawdata', '0002_alter_source_file'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rawdata',
            name='source_title',
        ),
        migrations.DeleteModel(
            name='Source',
        ),
    ]
