# Generated by Django 5.0.4 on 2024-04-16 00:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0007_alter_posting_author'),
        ('mypage', '0004_delete_mypost'),
        ('page1', '0003_profile'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
