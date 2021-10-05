# Generated by Django 3.2.7 on 2021-10-05 00:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Insumos', '0003_remove_ingrediente_unidades'),
        ('Usuarios', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CarritoCompras',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('dcto', models.FloatField(default=0)),
                ('cantMinima', models.IntegerField(default=0)),
                ('pagado', models.BooleanField(default=False)),
                ('usuario', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Usuarios.perfil')),
            ],
        ),
        migrations.CreateModel(
            name='infoEnvio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('apellido', models.CharField(max_length=200)),
                ('direccion', models.CharField(max_length=300)),
                ('paais', models.CharField(max_length=300)),
                ('departamento', models.CharField(max_length=300)),
                ('ciudad', models.CharField(max_length=300)),
                ('carrito', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Checkout.carritocompras')),
            ],
        ),
        migrations.CreateModel(
            name='Articulo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField()),
                ('carrito', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Checkout.carritocompras')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Insumos.producto')),
            ],
        ),
    ]
