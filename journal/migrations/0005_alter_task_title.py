# Generated by Django 4.0.5 on 2022-06-24 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('journal', '0004_alter_task_date_completed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='title',
            field=models.CharField(default='Create or Edit Task', max_length=120),
        ),
    ]