# Generated by Django 3.2.7 on 2021-10-06 20:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Insumos', '0005_ingrediente_unidades'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ingredientesesp',
            name='Ingredientes',
        ),
        migrations.AddField(
            model_name='ingredientesesp',
            name='cantidadEsp',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='MedidaIngrediente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.FloatField()),
                ('ingrediente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Insumos.ingrediente')),
                ('ingredienteEsp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Insumos.ingredientesesp')),
            ],
        ),
    ]
