# Generated by Django 4.2.5 on 2024-05-22 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_remove_user_courses_user_courses'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='courses',
            field=models.CharField(default='rfrf', max_length=300),
        ),
        migrations.AlterField(
            model_name='user',
            name='status',
            field=models.CharField(default='ccd', max_length=20),
        ),
    ]
