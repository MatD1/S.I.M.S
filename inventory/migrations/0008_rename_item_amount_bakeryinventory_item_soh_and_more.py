# Generated by Django 4.0.6 on 2022-07-19 14:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0007_alter_bakeryinventory_item_price_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bakeryinventory',
            old_name='Item_Amount',
            new_name='Item_SOH',
        ),
        migrations.RenameField(
            model_name='dairyinventory',
            old_name='Item_Amount',
            new_name='Item_SOH',
        ),
        migrations.RenameField(
            model_name='freshinventory',
            old_name='Item_Amount',
            new_name='Item_SOH',
        ),
        migrations.RenameField(
            model_name='groceryinventory',
            old_name='Item_Amount',
            new_name='Item_SOH',
        ),
    ]
