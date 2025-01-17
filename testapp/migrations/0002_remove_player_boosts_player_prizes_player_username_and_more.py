# Generated by Django 4.2.14 on 2024-08-01 11:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='player',
            name='boosts',
        ),
        migrations.AddField(
            model_name='player',
            name='prizes',
            field=models.ManyToManyField(related_name='players', to='testapp.prize'),
        ),
        migrations.AddField(
            model_name='player',
            name='username',
            field=models.CharField(blank=True, max_length=150),
        ),
        migrations.CreateModel(
            name='PlayerBoost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('boost', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testapp.boost')),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testapp.player')),
            ],
        ),
    ]
