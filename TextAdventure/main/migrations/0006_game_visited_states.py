# Generated by Django 5.0.1 on 2024-03-25 15:52

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0005_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="game",
            name="visited_states",
            field=models.TextField(default=""),
        ),
    ]
