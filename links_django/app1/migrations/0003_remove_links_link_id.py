# Generated by Django 4.1.5 on 2023-01-22 18:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_alter_links_link_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='links',
            name='link_id',
        ),
    ]
