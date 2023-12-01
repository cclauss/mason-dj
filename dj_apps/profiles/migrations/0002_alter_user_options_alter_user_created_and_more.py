# Generated by Django 4.2.7 on 2023-12-01 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'get_latest_by': 'created', 'ordering': ['-created']},
        ),
        migrations.AlterField(
            model_name='user',
            name='created',
            field=models.DateTimeField(editable=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='modified',
            field=models.DateTimeField(editable=False),
        ),
    ]
