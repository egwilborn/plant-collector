# Generated by Django 4.2.4 on 2023-08-16 22:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_pot_color_pot_material_pot_size'),
    ]

    operations = [
        migrations.AddField(
            model_name='plant',
            name='pots',
            field=models.ManyToManyField(to='main_app.pot'),
        ),
    ]
