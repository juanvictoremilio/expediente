# Generated by Django 4.0.6 on 2022-08-10 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consultorio', '0019_urgencias_hemodinamico'),
    ]

    operations = [
        migrations.RenameField(
            model_name='urgencias',
            old_name='PaFI',
            new_name='O2',
        ),
        migrations.RemoveField(
            model_name='urgencias',
            name='a1c',
        ),
        migrations.AddField(
            model_name='urgencias',
            name='FiO2',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, verbose_name='Temp'),
        ),
        migrations.AddField(
            model_name='urgencias',
            name='SpFI',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
    ]