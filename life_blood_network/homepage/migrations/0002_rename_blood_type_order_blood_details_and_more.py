# Generated by Django 5.0.6 on 2024-06-14 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("homepage", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="order",
            old_name="blood_type",
            new_name="blood_details",
        ),
        migrations.AlterField(
            model_name="order",
            name="quantity",
            field=models.IntegerField(default=1),
        ),
    ]
