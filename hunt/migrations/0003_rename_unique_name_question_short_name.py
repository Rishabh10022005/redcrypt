# Generated by Django 4.0.4 on 2022-06-07 11:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hunt', '0002_leveltracking_answerattempt'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='unique_name',
            new_name='short_name',
        ),
    ]
