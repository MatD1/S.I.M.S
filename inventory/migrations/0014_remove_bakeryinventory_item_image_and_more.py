# Generated by Django 4.0.6 on 2022-07-22 03:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0013_alter_bakeryinventory_item_image_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bakeryinventory',
            name='Item_Image',
        ),
        migrations.RemoveField(
            model_name='dairyinventory',
            name='Item_Image',
        ),
        migrations.RemoveField(
            model_name='deliinventory',
            name='Item_Image',
        ),
        migrations.RemoveField(
            model_name='freshinventory',
            name='Item_Image',
        ),
        migrations.RemoveField(
            model_name='groceryinventory',
            name='Item_Image',
        ),
        migrations.RemoveField(
            model_name='meatinventory',
            name='Item_Image',
        ),
    ]