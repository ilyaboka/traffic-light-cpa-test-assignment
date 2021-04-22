# Generated by Django 3.2 on 2021-04-17 12:35

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies: list = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                (
                    'department_id',
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ('department_name', models.CharField(max_length=128)),
                (
                    'parent',
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name='childern',
                        to='app.department',
                    ),
                ),
            ],
        ),
    ]