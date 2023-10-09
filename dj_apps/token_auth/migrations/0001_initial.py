# Generated by Django 4.2.6 on 2023-10-09 12:11

import core.utils.string_utils
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PasswordLessToken',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sid', models.CharField(db_index=True, default=core.utils.string_utils.get_secret_id, editable=False, unique=True)),
                ('created', models.DateTimeField(editable=False, verbose_name='Création')),
                ('modified', models.DateTimeField(editable=False, verbose_name='Modification')),
                ('end_of_validity', models.DateTimeField()),
                ('key', models.CharField(max_length=6, validators=[django.core.validators.MinLengthValidator(6), django.core.validators.MaxLengthValidator(6), django.core.validators.RegexValidator('^[0-9]*$', 'Only numeric characters are allowed.')])),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='passwordless_tokens', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'tb_password_less_tokens',
            },
        ),
        migrations.CreateModel(
            name='MagicLinkToken',
            fields=[
                ('created', models.DateTimeField(editable=False, verbose_name='Création')),
                ('modified', models.DateTimeField(editable=False, verbose_name='Modification')),
                ('key', models.CharField(editable=False, max_length=512, primary_key=True, serialize=False, unique=True)),
                ('end_of_validity', models.DateTimeField()),
                ('usage', models.CharField(choices=[('signup', 'Sign up'), ('login', 'Log in')], max_length=1024)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='magiclink_tokens', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'tb_magic_link_tokens',
            },
        ),
        migrations.CreateModel(
            name='APIToken',
            fields=[
                ('created', models.DateTimeField(editable=False, verbose_name='Création')),
                ('modified', models.DateTimeField(editable=False, verbose_name='Modification')),
                ('key', models.CharField(editable=False, max_length=512, primary_key=True, serialize=False, unique=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='api_token', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'tb_api_tokens',
            },
        ),
    ]
