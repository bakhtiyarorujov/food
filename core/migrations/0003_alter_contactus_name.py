# Generated by Django 5.0.6 on 2024-06-10 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_rename_meesage_contactus_message'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactus',
            name='name',
            field=models.CharField(max_length=100, unique=True, verbose_name='Ad'),
        ),
    ]
