# Generated by Django 3.2.4 on 2021-07-10 14:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rawdata', '0007_alter_nlp_token_rawdata_source_sentence'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Lemma',
        ),
    ]
