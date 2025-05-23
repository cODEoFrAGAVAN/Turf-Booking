# Generated by Django 5.2 on 2025-04-27 12:05

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_signup',
            name='unique_id',
            field=models.UUIDField(default=uuid.UUID('7c3dc344-5e65-4205-8519-ecd6cd096e0e'), primary_key=True, serialize=False),
        ),
        migrations.CreateModel(
            name='Random_token_generation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=30)),
                ('random_token', models.TextField()),
                ('unique_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.user_signup')),
            ],
        ),
    ]
