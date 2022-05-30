# Generated by Django 4.0.4 on 2022-05-30 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_alter_profile_user'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profile',
            options={'verbose_name_plural': 'User Progress'},
        ),
        migrations.AddField(
            model_name='profile',
            name='ip_address',
            field=models.JSONField(default={'ip_address': []}),
            preserve_default=False,
        ),
    ]
