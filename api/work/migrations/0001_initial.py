# Generated by Django 3.2.18 on 2024-03-13 15:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Muscles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='WorkOuts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=500)),
                ('instructions', models.CharField(default='', max_length=500)),
                ('recomended_sets', models.IntegerField(default=1)),
                ('recomended_rep', models.IntegerField(default=10)),
                ('target_muscles', models.ForeignKey(default=0, on_delete=django.db.models.deletion.DO_NOTHING, to='work.muscles')),
            ],
        ),
    ]