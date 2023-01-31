# Generated by Django 4.1.4 on 2022-12-28 04:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="movie_list",
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
                ("name", models.CharField(max_length=100)),
                ("year", models.IntegerField()),
                ("director", models.CharField(max_length=100)),
                ("img", models.ImageField(upload_to="images")),
            ],
        ),
    ]
