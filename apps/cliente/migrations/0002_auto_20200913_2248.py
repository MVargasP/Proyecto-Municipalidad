# Generated by Django 3.1.1 on 2020-09-14 03:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Documento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.BooleanField(default=True, verbose_name='Estado')),
                ('fecha_creacion', models.DateField(auto_now_add=True, verbose_name='Fecha de Creacion')),
                ('fecha_modificacion', models.DateField(auto_now=True, verbose_name='Fecha de Modificacion')),
                ('fecha_eliminacion', models.DateField(auto_now=True, verbose_name='Fecha de Eliminacion')),
                ('tipo', models.CharField(max_length=50, verbose_name='Tipo de Documento')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RenameField(
            model_name='cliente',
            old_name='dni',
            new_name='num_documento',
        ),
        migrations.AlterField(
            model_name='cliente',
            name='codigo',
            field=models.IntegerField(verbose_name='Codigo'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='empresa',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cliente.empresa'),
        ),
        migrations.AddField(
            model_name='cliente',
            name='documento',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cliente.documento'),
        ),
    ]