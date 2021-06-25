# Generated by Django 3.2.4 on 2021-06-25 13:41

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('original_text', '0009_alter_lemma_text'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='token',
            name='token_lemma',
        ),
        migrations.AddField(
            model_name='token',
            name='finished',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='token',
            name='note',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='token',
            name='priority',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='token',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Lemma',
        ),
    ]
