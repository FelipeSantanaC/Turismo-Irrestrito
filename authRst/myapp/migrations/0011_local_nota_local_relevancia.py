# Generated by Django 4.2.2 on 2023-07-15 03:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0010_remove_local_nota"),
    ]

    operations = [
        migrations.AddField(
            model_name="local",
            name="nota",
            field=models.DecimalField(decimal_places=1, default=0.0, max_digits=2),
        ),
        migrations.AddField(
            model_name="local",
            name="relevancia",
            field=models.IntegerField(default=0),
        ),
    ]