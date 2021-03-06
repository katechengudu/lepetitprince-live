# Generated by Django 3.2.4 on 2021-06-28 12:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('original_text', '0019_auto_20210628_2044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sentence',
            name='book_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='original_text.book'),
        ),
        migrations.AlterField(
            model_name='token',
            name='book_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='original_text.book'),
        ),
    ]
