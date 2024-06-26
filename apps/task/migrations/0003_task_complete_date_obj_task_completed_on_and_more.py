# Generated by Django 5.0.4 on 2024-04-30 13:26

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("task", "0002_section_user"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name="task",
            name="complete_date_obj",
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name="task",
            name="completed_on",
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name="task",
            name="created_by",
            field=models.ForeignKey(
                default=None,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="created_tasks",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="task",
            name="is_public",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="task",
            name="relies_on",
            field=models.ManyToManyField(blank=True, to="task.task"),
        ),
        migrations.AddField(
            model_name="task",
            name="value",
            field=models.IntegerField(default=0),
        ),
    ]
