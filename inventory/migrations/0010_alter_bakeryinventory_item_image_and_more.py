# Generated by Django 4.0.6 on 2022-07-21 01:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0009_bakeryinventory_item_image_dairyinventory_item_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bakeryinventory',
            name='Item_Image',
            field=models.ImageField(default='assets/S.I.M.S.png', upload_to='assets/'),
        ),
        migrations.AlterField(
            model_name='dairyinventory',
            name='Item_Image',
            field=models.ImageField(default='assets/S.I.M.S.png', upload_to='assets/'),
        ),
        migrations.AlterField(
            model_name='freshinventory',
            name='Item_Image',
            field=models.ImageField(default='assets/S.I.M.S.png', upload_to='assets/'),
        ),
        migrations.AlterField(
            model_name='groceryinventory',
            name='Item_Image',
            field=models.ImageField(default='assets/S.I.M.S.png', upload_to='assets/'),
        ),
    ]
