# Generated by Django 2.2.5 on 2020-01-17 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_auto_20200117_0216'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='video_url',
            field=models.CharField(max_length=50),
        ),
    ]
