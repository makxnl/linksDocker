# Generated by Django 4.1.5 on 2023-01-23 20:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_remove_links_link_id'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Links',
        ),
    ]
