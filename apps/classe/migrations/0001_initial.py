# Generated by Django 4.2 on 2023-05-19 11:59

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Classe",
            fields=[
                ("id_classe", models.AutoField(primary_key=True, serialize=False)),
                ("nome", models.CharField(max_length=50)),
            ],
            options={
                "verbose_name": "Classe",
                "verbose_name_plural": "Classes",
                "db_table": "classe",
            },
        ),
    ]
