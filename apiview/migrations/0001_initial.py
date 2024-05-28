# Generated by Django 5.0.6 on 2024-05-27 17:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'category',
            },
        ),
        migrations.CreateModel(
            name='MusicKlip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('video', models.FileField(blank=True, null=True, upload_to='videos/')),
                ('audio', models.FileField(blank=True, null=True, upload_to='audio/')),
                ('docPDF', models.FileField(null=True, upload_to='doc/')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apiview.category')),
            ],
            options={
                'db_table': 'music_klip',
            },
        ),
    ]