# Generated by Django 3.2.4 on 2021-06-25 06:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('original_text', '0002_remove_sentence_paragraph_title'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Paragraph',
        ),
    ]
