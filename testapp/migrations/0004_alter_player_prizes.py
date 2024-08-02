# Generated by Django 4.2.14 on 2024-08-01 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0003_alter_player_prizes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='prizes',
            field=models.ManyToManyField(blank=True, null=True, related_name='players', to='testapp.prize'),
        ),
    ]
