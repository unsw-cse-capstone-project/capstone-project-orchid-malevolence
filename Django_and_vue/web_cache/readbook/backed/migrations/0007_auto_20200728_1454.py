# Generated by Django 3.0.7 on 2020-07-28 14:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('backed', '0006_goal_accomplish_nums'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='goal',
            name='accomplish_nums',
        ),
        migrations.CreateModel(
            name='MonthRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.PositiveIntegerField(default=0)),
                ('month', models.PositiveIntegerField(default=0)),
                ('total_nums', models.PositiveIntegerField(default=0)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_record', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('user', 'year', 'month')},
            },
        ),
    ]