# Generated by Django 3.0.8 on 2020-09-01 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_profile_nickname'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='followers',
            field=models.ManyToManyField(related_name='follows', to='accounts.Profile'),
        ),
    ]