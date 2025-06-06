# Generated by Django 5.1.7 on 2025-03-27 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='course_type',
            field=models.CharField(choices=[('lecture', 'Лекция'), ('seminar', 'Семинар'), ('lab', 'Лабораторная работа')], default='lecture', max_length=10),
        ),
        migrations.AddField(
            model_name='course',
            name='credits',
            field=models.PositiveSmallIntegerField(default=3),
        ),
        migrations.AddField(
            model_name='course',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]
