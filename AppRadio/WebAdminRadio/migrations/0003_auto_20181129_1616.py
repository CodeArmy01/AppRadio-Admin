# Generated by Django 2.1.1 on 2018-11-29 21:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('WebAdminRadio', '0002_auto_20181019_1250'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='frecuencia',
            name='duracion',
        ),
        migrations.RemoveField(
            model_name='frecuencia',
            name='nro_dias',
        ),
        migrations.RemoveField(
            model_name='frecuencia_publicidad',
            name='idSegmento',
        ),
        migrations.AddField(
            model_name='frecuencia_publicidad',
            name='idPublicidad',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='WebAdminRadio.Publicidad'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='frecuencia',
            name='tipo',
            field=models.CharField(max_length=8),
        ),
        migrations.AlterField(
            model_name='publicidad',
            name='estado',
            field=models.CharField(default='A', max_length=1),
        ),
    ]
