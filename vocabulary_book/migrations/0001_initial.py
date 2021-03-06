# Generated by Django 3.2.4 on 2021-07-06 17:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('original_text', '0020_auto_20210628_2045'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyWord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mynote4review', models.CharField(max_length=500)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('related_token_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='related_token', to='original_text.token')),
                ('token_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='original_text.token')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
