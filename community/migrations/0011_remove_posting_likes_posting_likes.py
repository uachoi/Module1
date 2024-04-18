# Generated by Django 5.0.4 on 2024-04-16 09:14

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0010_remove_posting_likes_posting_likes'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='posting',
            name='likes',
        ),
        migrations.AddField(
            model_name='posting',
            name='likes',
            field=models.ManyToManyField(related_name='posting_like', to=settings.AUTH_USER_MODEL),
        ),
    ]
