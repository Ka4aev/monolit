# Generated by Django 5.1.1 on 2024-10-30 18:23

import django.contrib.auth.models
import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


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
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('last_name', models.CharField(max_length=254, verbose_name='Фамилия')),
                ('first_name', models.CharField(max_length=254, verbose_name='Имя')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Почта')),
                ('username', models.CharField(max_length=254, unique=True, verbose_name='Логин')),
                ('password', models.CharField(max_length=254, verbose_name='Пароль')),
                ('avatar', models.ImageField(upload_to='polls/user', verbose_name='Фото профиля')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=250, verbose_name='Вопрос')),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('short_description', models.CharField(max_length=450, null=True)),
                ('description', models.CharField(max_length=1500, null=True)),
                ('image', models.ImageField(blank=True, upload_to='polls/questions')),
                ('votes', models.IntegerField(blank=True, default=0)),
                ('voted_by', models.ManyToManyField(blank=True, related_name='voted_by', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice_text', models.CharField(max_length=200, verbose_name='Вариант ответа')),
                ('votes', models.IntegerField(default=0, verbose_name='Голоса')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.question')),
            ],
        ),
    ]
