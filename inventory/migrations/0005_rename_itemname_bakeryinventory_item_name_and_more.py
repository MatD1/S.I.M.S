# Generated by Django 4.0.6 on 2022-07-19 04:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0004_alter_bakeryinventory_options_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bakeryinventory',
            old_name='ItemName',
            new_name='Item_Name',
        ),
        migrations.RenameField(
            model_name='dairyinventory',
            old_name='ItemName',
            new_name='Item_Name',
        ),
        migrations.RenameField(
            model_name='freshinventory',
            old_name='ItemName',
            new_name='Item_Name',
        ),
        migrations.RenameField(
            model_name='groceryinventory',
            old_name='ItemName',
            new_name='Item_Name',
        ),
    ]
