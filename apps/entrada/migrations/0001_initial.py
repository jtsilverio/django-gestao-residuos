# Generated by Django 4.2.6 on 2023-11-01 00:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("classe", "0001_initial"),
        ("cluster", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Entrada",
            fields=[
                ("id_entrada", models.AutoField(primary_key=True, serialize=False)),
                ("data", models.DateField()),
                (
                    "peso",
                    models.DecimalField(decimal_places=2, default=0, max_digits=10),
                ),
                (
                    "id_classe",
                    models.ForeignKey(
                        db_column="id_classe",
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="classe.classe",
                    ),
                ),
                (
                    "id_cluster",
                    models.ForeignKey(
                        db_column="id_cluster",
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="cluster.cluster",
                    ),
                ),
            ],
            options={
                "db_table": "entrada",
                "ordering": ["-id_entrada"],
            },
        ),
    ]
