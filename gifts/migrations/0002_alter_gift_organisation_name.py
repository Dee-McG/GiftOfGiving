# Generated by Django 4.0 on 2021-12-12 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gifts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gift',
            name='organisation_name',
            field=models.CharField(max_length=150),
        ),
    ]