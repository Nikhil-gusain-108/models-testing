# Generated by Django 5.0.6 on 2024-07-04 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviews',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='user_details',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
