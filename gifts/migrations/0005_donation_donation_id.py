# Generated by Django 3.2 on 2021-12-11 17:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gifts', '0004_alter_gift_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='donation',
            name='donation_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='gifts.gift'),
        ),
    ]