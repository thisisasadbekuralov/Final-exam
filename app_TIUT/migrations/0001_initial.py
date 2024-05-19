# Generated by Django 5.0.4 on 2024-05-19 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FAQ',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FAQ_name_uz', models.CharField(max_length=100)),
                ('FAQ_name_en', models.CharField(max_length=100)),
                ('answer_uz', models.TextField()),
                ('answer_en', models.TextField()),
            ],
            options={
                'verbose_name': 'FAQ',
                'verbose_name_plural': 'FAQs',
                'db_table': 'FAQ',
            },
        ),
        migrations.CreateModel(
            name='Paper',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paper_title_uz', models.CharField(max_length=100)),
                ('paper_title_en', models.CharField(max_length=100)),
                ('paper_text_uz', models.TextField()),
                ('paper_text_en', models.TextField()),
                ('paper_file_uz', models.FileField(blank=True, null=True, upload_to='papers/')),
                ('paper_file_en', models.FileField(blank=True, null=True, upload_to='papers/')),
                ('paper_keywords_uz', models.CharField(max_length=100)),
                ('paper_keywords_en', models.CharField(max_length=100)),
                ('views_count', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name': 'Paper',
                'db_table': 'paper',
            },
        ),
        migrations.CreateModel(
            name='Publication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pub_name_uz', models.CharField(max_length=100)),
                ('pub_name_en', models.CharField(max_length=100)),
                ('pub_description_uz', models.TextField()),
                ('pub_description_en', models.TextField()),
                ('pub_file_uz', models.FileField(blank=True, null=True, upload_to='publications/')),
                ('pub_file_en', models.FileField(blank=True, null=True, upload_to='publications/')),
                ('image', models.ImageField(upload_to='publications/')),
                ('views_count', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name': 'Publication',
                'db_table': 'publication',
            },
        ),
        migrations.CreateModel(
            name='Requirements',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('requirements_parts_uz', models.CharField(max_length=100)),
                ('requirements_parts_en', models.CharField(max_length=100)),
                ('requirements_title_uz', models.TextField()),
                ('requirements_title_en', models.TextField()),
                ('requirements_description_uz', models.TextField()),
                ('requirements_description_en', models.TextField()),
            ],
            options={
                'verbose_name': 'Requirement',
                'verbose_name_plural': 'Requirements',
                'db_table': 'Requirements',
            },
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review_text', models.TextField()),
                ('review_file', models.FileField(null=True, upload_to='reviews/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Review',
                'verbose_name_plural': 'Reviews',
                'db_table': 'reviews',
            },
        ),
        migrations.CreateModel(
            name='Sphere',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_uz', models.CharField(max_length=100)),
                ('name_en', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Sphere',
                'db_table': 'sphere',
            },
        ),
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
