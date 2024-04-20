# Generated by Django 5.0.4 on 2024-04-09 05:21

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Sprint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=50, null=True)),
                ('description', models.TextField(default='', max_length=150, null=True)),
                ('end_date', models.DateTimeField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField(default='', max_length=150, null=True)),
                ('status', models.SmallIntegerField(choices=[(1, 'Not Started'), (2, 'WORKING ON'), (3, 'TESTING'), (4, 'FINISHED')], default='STATUS_TODO')),
                ('order', models.SmallIntegerField(default=0)),
                ('start_date', models.DateTimeField(null=True)),
                ('due_date', models.DateTimeField(null=True)),
                ('completed_date', models.DateTimeField(null=True)),
                ('assigned', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('sprint', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='board.sprint')),
            ],
        ),
    ]