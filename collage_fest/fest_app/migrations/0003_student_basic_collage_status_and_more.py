# Generated by Django 5.0.1 on 2024-03-07 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fest_app', '0002_student_basic_payment_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='student_basic',
            name='collage_status',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student_basic',
            name='college_name',
            field=models.CharField(default=0, max_length=300),
            preserve_default=False,
        ),
    ]
