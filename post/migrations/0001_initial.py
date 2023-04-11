# Generated by Django 4.1.7 on 2023-04-01 07:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Post",
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
                ("title", models.CharField(max_length=256)),
                ("content", models.TextField()),
                (
                    "created_at",
                    models.DateTimeField(
                        default=datetime.datetime(
                            2023, 4, 1, 7, 17, 43, 812887, tzinfo=datetime.timezone.utc
                        )
                    ),
                ),
            ],
        ),
    ]
