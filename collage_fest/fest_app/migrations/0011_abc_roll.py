# Generated by Django 5.0.1 on 2024-03-13 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fest_app', '0010_abc_rename_event_id_events_detalis_roll_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='abc',
            name='roll',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
