# Generated by Django 5.0.4 on 2024-05-20 05:02

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('app_TIUT', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='paper',
            name='reviews',
            field=models.ManyToManyField(related_name='paper_reviews', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='review',
            name='paper',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='review_set', to='app_TIUT.paper'),
        ),
        migrations.AddField(
            model_name='review',
            name='reviewer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='reviewreviewer',
            name='review',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_TIUT.review'),
        ),
        migrations.AddField(
            model_name='reviewreviewer',
            name='reviewer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='publication',
            name='pub_sphere',
            field=models.ManyToManyField(related_name='publications', to='app_TIUT.sphere'),
        ),
        migrations.AddField(
            model_name='paper',
            name='paper_sphere',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_TIUT.sphere'),
        ),
        migrations.AlterUniqueTogether(
            name='review',
            unique_together={('paper', 'reviewer')},
        ),
        migrations.AlterUniqueTogether(
            name='reviewreviewer',
            unique_together={('review', 'reviewer')},
        ),
    ]
