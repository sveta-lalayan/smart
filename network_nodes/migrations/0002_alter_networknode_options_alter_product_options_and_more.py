

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("network_nodes", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="networknode",
            options={
                "ordering": ["name"],
                "verbose_name": "Предприятие",
                "verbose_name_plural": "Предприятия",
            },
        ),
        migrations.AlterModelOptions(
            name="product",
            options={
                "ordering": ["name"],
                "verbose_name": "Продукт",
                "verbose_name_plural": "Продукты",
            },
        ),
        migrations.AddIndex(
            model_name="networknode",
            index=models.Index(fields=["name"], name="network_nod_name_4946f9_idx"),
        ),
        migrations.AddIndex(
            model_name="product",
            index=models.Index(fields=["name"], name="network_nod_name_fa3b44_idx"),
        ),
    ]
