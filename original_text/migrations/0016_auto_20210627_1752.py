# Generated by Django 3.2.4 on 2021-06-27 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('original_text', '0015_token_chapter_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='token',
            name='sentence_number',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='token',
            name='token_language',
            field=models.CharField(default='french', max_length=100),
        ),
        migrations.AddField(
            model_name='token',
            name='token_nunmber',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
