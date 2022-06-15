# Generated by Django 4.0.5 on 2022-06-15 06:50

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('text', models.CharField(max_length=60)),
                ('date_created', models.DateField(default=datetime.date.today, null=True, verbose_name='creation date')),
                ('priority', models.IntegerField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['priority'],
            },
        ),
        migrations.CreateModel(
            name='DayView',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('date_created', models.DateField(default=datetime.date.today, verbose_name='creation date')),
                ('top_priorities', models.TextField()),
                ('hydration_log', models.TextField()),
                ('meals_log', models.TextField()),
                ('meditation_log', models.BooleanField(default=False)),
                ('schedule', models.TextField()),
                ('day_planning', models.TextField()),
                ('day_review', models.TextField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('today_todos', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='journal.task')),
            ],
        ),
    ]