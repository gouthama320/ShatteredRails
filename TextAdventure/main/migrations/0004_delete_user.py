# Generated by Django 5.0.1 on 2024-02-21 14:18

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0003_user_email_user_name_delete_userprofile"),
    ]

    operations = [
        migrations.DeleteModel(
            name="User",
        ),
    ]
