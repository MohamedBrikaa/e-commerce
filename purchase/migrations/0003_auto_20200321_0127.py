# Generated by Django 3.0.3 on 2020-03-21 01:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('purchase', '0002_auto_20200320_0409'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase',
            name='cartUser',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]