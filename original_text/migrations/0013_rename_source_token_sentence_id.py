# Generated by Django 3.2.4 on 2021-06-27 06:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('original_text', '0012_auto_20210627_1410'),
    ]

    operations = [
        migrations.RenameField(
            model_name='token',
            old_name='source',
            new_name='sentence_id',
        ),
    ]
