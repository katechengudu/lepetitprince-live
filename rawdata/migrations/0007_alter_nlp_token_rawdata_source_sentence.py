# Generated by Django 3.2.4 on 2021-07-10 13:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rawdata', '0006_alter_rawdata_source_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nlp_token_rawdata',
            name='source_sentence',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='rawdata.rawdata'),
        ),
    ]
