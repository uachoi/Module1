# Generated by Django 5.0.4 on 2024-04-22 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0013_remove_posting_likes_like'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='is_del',
            field=models.BooleanField(default=False),
        ),
    ]
