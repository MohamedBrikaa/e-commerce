# Generated by Django 3.0.3 on 2020-03-18 17:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_auto_20200317_1805'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sub_category',
            name='sub_cat_img',
        ),
    ]
