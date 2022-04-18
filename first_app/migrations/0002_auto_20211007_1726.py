# Generated by Django 3.2.8 on 2021-10-07 11:26

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='ts_created',
            field=models.DateTimeField(db_index=True, default=django.utils.timezone.now, editable=False),
        ),
        migrations.AddField(
            model_name='student',
            name='ts_updated',
            field=models.DateTimeField(auto_now=True, db_index=True),
        ),
    ]
