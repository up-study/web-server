# Generated by Django 4.1.3 on 2023-02-05 16:14

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ("base", "0002_initial"),
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="email_notifications",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="user",
            name="profile_photo",
            field=models.ForeignKey(
                null=True, on_delete=django.db.models.deletion.CASCADE, to="base.image"
            ),
        ),
        migrations.AddField(
            model_name="user",
            name="tg_notifications",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="user",
            name="uuid",
            field=models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
        ),
        migrations.AddField(
            model_name="user",
            name="wa_notifications",
            field=models.BooleanField(default=False),
        ),
    ]
