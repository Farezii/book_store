# Generated by Django 5.0.1 on 2024-02-05 13:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book_outlet', '0007_country_alter_address_options_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='published_contries',
            new_name='published_countries',
        ),
    ]
