# Generated by Django 5.2.1 on 2025-05-21 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desc', models.TextField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
