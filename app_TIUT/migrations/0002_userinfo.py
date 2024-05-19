# Generated by Django 5.0.4 on 2024-05-19 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_TIUT', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('message', models.TextField()),
            ],
            options={
                'verbose_name': 'User',
                'db_table': 'userinfo',
            },
        ),
    ]
