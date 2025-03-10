# Generated by Django 5.0.7 on 2025-02-20 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0007_alter_person_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='category',
            field=models.CharField(blank=True, choices=[('P', 'Postgraduate'), ('M', 'MSC'), ('U', 'Undergraduate'), ('A', 'Admin'), ('I', 'PI'), ('L', 'Lecturer'), ('C', 'Currentundergraduate')], max_length=1, null=True, verbose_name='Category'),
        ),
    ]
