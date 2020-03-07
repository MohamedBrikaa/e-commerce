# Generated by Django 3.0.3 on 2020-03-06 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('email', models.EmailField(editable='true', max_length=254, null='false')),
                ('phone', models.CharField(editable='true', max_length=11)),
                ('gender', models.CharField(max_length=20)),
                ('birthDate', models.DateField()),
                ('address1', models.TextField(editable='true')),
                ('address2', models.TextField(editable='true')),
                ('creditNumber', models.CharField(editable='true', max_length=19)),
                ('image', models.ImageField(upload_to='user_imgs')),
            ],
        ),
    ]
