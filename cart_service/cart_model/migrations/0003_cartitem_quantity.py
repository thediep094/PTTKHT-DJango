# Generated by Django 4.1.7 on 2023-04-05 02:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart_model', '0002_rename_apparel_id_cartitem_itemtype_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartitem',
            name='quantity',
            field=models.IntegerField(default=0),
        ),
    ]
