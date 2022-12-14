# Generated by Django 4.1.4 on 2022-12-14 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("category", "0001_initial"),
        ("todo", "0002_todo_created_at_todo_updated_at_alter_todo_user"),
    ]

    operations = [
        migrations.AddField(
            model_name="todo",
            name="category",
            field=models.ManyToManyField(
                blank=True, related_name="categories", to="category.category"
            ),
        ),
    ]
