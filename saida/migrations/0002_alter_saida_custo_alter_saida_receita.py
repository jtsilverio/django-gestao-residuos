# Generated by Django 4.1.7 on 2023-04-03 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("saida", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="saida",
            name="custo",
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AlterField(
            model_name="saida",
            name="receita",
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]
