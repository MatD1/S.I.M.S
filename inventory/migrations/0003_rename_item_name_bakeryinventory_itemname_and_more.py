# Generated by Django 4.0.6 on 2022-07-19 04:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0002_remove_bakeryinventory_item_last_recieved_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bakeryinventory',
            old_name='Item_Name',
            new_name='ItemName',
        ),
        migrations.RenameField(
            model_name='dairyinventory',
            old_name='Item_Name',
            new_name='ItemName',
        ),
        migrations.RenameField(
            model_name='freshinventory',
            old_name='Item_Name',
            new_name='ItemName',
        ),
        migrations.RenameField(
            model_name='groceryinventory',
            old_name='Item_Name',
            new_name='ItemName',
        ),
    ]
