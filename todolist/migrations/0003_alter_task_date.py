# Generated by Django 4.1 on 2022-09-27 03:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0002_rename_data_task_date_task_is_finished'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]