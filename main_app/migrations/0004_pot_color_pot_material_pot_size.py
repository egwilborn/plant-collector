# Generated by Django 4.2.4 on 2023-08-16 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_pot_alter_watering_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='pot',
            name='color',
            field=models.CharField(default='blank', max_length=100),
        ),
        migrations.AddField(
            model_name='pot',
            name='material',
            field=models.CharField(default='blank', max_length=100),
        ),
        migrations.AddField(
            model_name='pot',
            name='size',
            field=models.CharField(default='blank', max_length=100),
        ),
    ]
