# Generated by Django 5.0.4 on 2024-04-24 18:53

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0002_customuser_phone"),
    ]

    operations = [
        migrations.AddField(
            model_name="customuser",
            name="is_admin",
            field=models.BooleanField(default=False),
        ),
    ]
