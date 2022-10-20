# Generated by Django 4.0.2 on 2022-10-12 19:22

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0002_alter_todo_uid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='uid',
            field=models.UUIDField(default=uuid.UUID('d7b12d3b-c290-4f59-9d1f-f838281be72c'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.CreateModel(
            name='TimingTodo',
            fields=[
                ('uid', models.UUIDField(default=uuid.UUID('d7b12d3b-c290-4f59-9d1f-f838281be72c'), editable=False, primary_key=True, serialize=False)),
                ('timing', models.DateField()),
                ('todo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='first_app.todo')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
