# Generated by Django 4.0.4 on 2022-08-03 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0024_alter_profile_avatar_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar_url',
            field=models.CharField(default='https://source.boringavatars.com/beam/512/redcrypt?colors=00D2D2,006D6D,002A2A,055D5D,074848&square', max_length=150),
        ),
    ]
