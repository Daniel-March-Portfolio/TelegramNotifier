# Generated by Django 5.2b1 on 2025-03-02 14:59

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TelegramBot',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=64)),
                ('token', models.CharField(max_length=64)),
            ],
        ),
    ]
