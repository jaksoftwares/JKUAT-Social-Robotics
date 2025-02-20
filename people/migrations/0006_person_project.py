# Generated by Django 5.0.7 on 2024-08-13 03:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0005_alter_person_personal_website_link'),
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='project',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='projects.project', verbose_name='Project'),
        ),
    ]
