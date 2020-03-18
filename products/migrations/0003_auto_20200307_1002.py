# Generated by Django 3.0.3 on 2020-03-07 10:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20200306_2133'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='favourite',
            unique_together=None,
        ),
        migrations.RemoveField(
            model_name='favourite',
            name='product',
        ),
        migrations.RemoveField(
            model_name='favourite',
            name='user',
        ),
        migrations.AlterUniqueTogether(
            name='reviews',
            unique_together=None,
        ),
        migrations.RemoveField(
            model_name='reviews',
            name='product',
        ),
        migrations.RemoveField(
            model_name='reviews',
            name='user',
        ),
        migrations.DeleteModel(
            name='Comments',
        ),
        migrations.DeleteModel(
            name='Favourite',
        ),
        migrations.DeleteModel(
            name='Reviews',
        ),
    ]