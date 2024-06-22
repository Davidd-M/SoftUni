# Generated by Django 5.0.4 on 2024-06-21 08:51

from django.db import migrations


def set_rarity(apps, schema_editor):
    item_model = apps.get_model("main_app", "Item")
    items = item_model.objects.all()

    for item_record in items:
        if item_record.price <= 10:
            item_record.rarity = "Rare"
        elif 11 <= item_record.price <= 20:
            item_record.rarity = "Very Rare"
        elif 21 <= item_record.price <= 30:
            item_record.rarity = "Extremely Rare"
        elif item_record.price >= 31:
            item_record.rarity = "Mega Rare"

    item_model.objects.bulk_update(items, ["rarity"])


def set_rarity_default(apps, schema_editor):
    item_model = apps.get_model("main_app", "Item")
    items = item_model.objects.all()
    rarity_default = item_model._meta.get_field("rarity").default

    for item_record in items:
        item_record.rarity = rarity_default

    item_model.objects.bulk_update(items, ["rarity"])


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0011_item'),
    ]

    operations = [
        migrations.RunPython(set_rarity, set_rarity_default)
    ]