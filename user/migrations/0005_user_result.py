# Generated by Django 3.2.5 on 2021-07-11 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_alter_user_travel_history'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='result',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]
