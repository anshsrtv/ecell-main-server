# Generated by Django 3.0.5 on 2020-05-01 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iportal', '0010_auto_20200423_0040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='brief',
            field=models.CharField(max_length=200),
        ),
    ]