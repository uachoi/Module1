# Generated by Django 5.0.4 on 2024-04-16 01:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0007_alter_posting_author'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='categ',
            new_name='name',
        ),
    ]
