# Generated by Django 3.2.13 on 2022-05-30 21:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login_singup_page', '0004_auto_20220527_0003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='country',
            field=models.CharField(max_length=30),
        ),
    ]