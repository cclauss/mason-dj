# Generated by Django 4.2.6 on 2023-10-10 17:21

import core.utils.string_utils
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Badge',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True)),
                ('sid', models.CharField(db_index=True, default=core.utils.string_utils.get_secret_id, editable=False, unique=True)),
                ('created', models.DateTimeField(editable=False, verbose_name='Création')),
                ('modified', models.DateTimeField(editable=False, verbose_name='Modification')),
                ('expiration', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'tb_badges',
            },
        ),
    ]
