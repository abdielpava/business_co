# Generated by Django 3.2.7 on 2021-10-05 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Insumos', '0004_rename_nombreingrediente_ingredientesesp_ingredientes'),
    ]

    operations = [
        migrations.AddField(
            model_name='ingrediente',
            name='unidades',
            field=models.CharField(default='g', max_length=200),
        ),
    ]