# Generated by Django 5.0.7 on 2024-08-07 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0003_person_linked_in_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='personal_website_link',
            field=models.URLField(default='', verbose_name='Personal Website Link'),
            preserve_default=False,
        ),
    ]
