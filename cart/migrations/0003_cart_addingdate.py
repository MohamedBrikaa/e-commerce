# Generated by Django 3.0.3 on 2020-03-18 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0002_remove_cart_addingdate'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='addingDate',
            field=models.DateField(auto_now=True),
        ),
    ]
