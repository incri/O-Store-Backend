# Generated by Django 4.2.1 on 2023-05-15 08:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("store", "0003_rename_customer_customers_and_more"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Customers",
            new_name="Customer",
        ),
        migrations.RemoveIndex(
            model_name="customer",
            name="store_custo_last_na_2e448d_idx",
        ),
        migrations.AlterModelTable(
            name="customer",
            table=None,
        ),
    ]
