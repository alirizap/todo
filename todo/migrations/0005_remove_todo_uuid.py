# Generated by Django 4.1.4 on 2022-12-14 16:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("todo", "0004_todo_slug_todo_uuid"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="todo",
            name="uuid",
        ),
    ]
