# Generated by Django 4.1 on 2022-10-11 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Article",
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
                (
                    "title",
                    models.CharField(
                        default="Новость дня", max_length=250, verbose_name="Название"
                    ),
                ),
                (
                    "description",
                    models.CharField(
                        default="Новость дня", max_length=250, verbose_name="Название"
                    ),
                ),
            ],
        ),
    ]