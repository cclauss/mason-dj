# Generated by Django 4.2.6 on 2023-10-08 10:31

import core.utils.string_utils
from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('sid', models.CharField(db_index=True, default=core.utils.string_utils.get_secret_id, editable=False, max_length=128, unique=True)),
                ('created', models.DateTimeField(editable=False, verbose_name='Création')),
                ('modified', models.DateTimeField(editable=False, verbose_name='Modification')),
                ('is_active', models.BooleanField(default=True)),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='e-mail')),
                ('title', models.CharField(choices=[('MLLE', 'mademoiselle'), ('MME', 'madame'), ('M', 'monsieur')], max_length=128, verbose_name='civilité')),
                ('first_name', models.CharField(max_length=150, verbose_name='prénom')),
                ('last_name', models.CharField(max_length=150, verbose_name='nom')),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None, verbose_name='téléphone')),
                ('birth_date', models.DateField(blank=True, null=True, verbose_name='date de naissance')),
                ('is_staff', models.BooleanField(default=False, verbose_name='staff ?')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'utilisateur',
                'ordering': ['-created'],
                'get_latest_by': 'created',
            },
        ),
    ]
