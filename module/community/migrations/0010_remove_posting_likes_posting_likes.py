# Generated by Django 5.0.4 on 2024-04-16 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0009_alter_comment_author_alter_comment_post'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='posting',
            name='likes',
        ),
        migrations.AddField(
            model_name='posting',
            name='likes',
            field=models.IntegerField(default=0),
        ),
    ]
