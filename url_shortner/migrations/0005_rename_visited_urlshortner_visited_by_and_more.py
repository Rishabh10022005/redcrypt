# Generated by Django 4.0.4 on 2022-07-30 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('url_shortner', '0004_urlshortner_visited'),
    ]

    operations = [
        migrations.RenameField(
            model_name='urlshortner',
            old_name='visited',
            new_name='visited_by',
        ),
        migrations.AlterField(
            model_name='urlshortner',
            name='short_url',
            field=models.CharField(max_length=150, unique=True),
        ),
    ]