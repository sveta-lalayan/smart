

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="NetworkNode",
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
                ("name", models.CharField(max_length=100, verbose_name="Название")),
                ("email", models.EmailField(max_length=254, verbose_name="Email")),
                ("country", models.CharField(max_length=100, verbose_name="Страна")),
                ("city", models.CharField(max_length=100, verbose_name="Город")),
                ("street", models.CharField(max_length=100, verbose_name="Улица")),
                (
                    "building_number",
                    models.CharField(max_length=10, verbose_name="Номер дома"),
                ),
                (
                    "debt",
                    models.DecimalField(
                        decimal_places=2,
                        default=0.0,
                        max_digits=10,
                        verbose_name="Задолженность",
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Время создания"
                    ),
                ),
                (
                    "type",
                    models.CharField(
                        choices=[
                            ("factory", "Завод"),
                            ("retail", "Розничная сеть"),
                            ("entrepreneur", "Индивидуальный предприниматель"),
                        ],
                        default="retail",
                        max_length=15,
                        verbose_name="Тип",
                    ),
                ),
                (
                    "supplier",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="network_nodes.networknode",
                        verbose_name="Поставщик",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Product",
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
                ("name", models.CharField(max_length=100, verbose_name="Название")),
                ("model", models.CharField(max_length=100, verbose_name="Модель")),
                ("release_date", models.DateField(verbose_name="Дата выхода на рынок")),
                (
                    "supplier",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="products",
                        to="network_nodes.networknode",
                        verbose_name="Поставщик",
                    ),
                ),
            ],
        ),
    ]
