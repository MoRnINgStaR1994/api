# Generated by Django 3.2.18 on 2024-03-13 15:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jwtauth', '0002_auto_20240313_1445'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='workouts',
            name='target_muscles',
        ),
        migrations.DeleteModel(
            name='Muscles',
        ),
        migrations.DeleteModel(
            name='WorkOuts',
        ),
    ]
