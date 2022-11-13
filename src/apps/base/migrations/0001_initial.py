# Generated by Django 4.1.2 on 2022-11-04 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Image",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("photo", models.ImageField(upload_to="", verbose_name="Image")),
            ],
            options={
                "verbose_name_plural": "Image",
            },
        ),
    ]