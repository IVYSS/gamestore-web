# Generated by Django 2.2.11 on 2020-03-10 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gamehome', '0005_auto_20200311_0130'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='id',
        ),
        migrations.AddField(
            model_name='user',
            name='user_id',
            field=models.IntegerField(default=0, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='game',
            name='game_id',
            field=models.IntegerField(default=0, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='game_type',
            name='type_id',
            field=models.IntegerField(default=0, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='lmage',
            name='lmage_id',
            field=models.IntegerField(default=0, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='user_games',
            name='user_game_id',
            field=models.IntegerField(default=0, primary_key=True, serialize=False),
        ),
    ]
