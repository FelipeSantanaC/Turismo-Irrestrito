# Generated by Django 4.2.2 on 2023-07-05 03:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="myuser",
            name="is_admin",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="myuser",
            name="is_staff",
            field=models.BooleanField(default=False),
        ),
    ]