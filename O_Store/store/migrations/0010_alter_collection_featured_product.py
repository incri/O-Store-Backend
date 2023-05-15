# Generated by Django 4.2.1 on 2023-05-15 12:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("store", "0009_alter_promotion_options"),
    ]

    operations = [
        migrations.AlterField(
            model_name="collection",
            name="featured_product",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="+",
                to="store.product",
            ),
        ),
    ]