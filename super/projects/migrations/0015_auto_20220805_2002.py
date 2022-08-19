# Generated by Django 3.2.12 on 2022-08-05 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0014_rename_head_technical_profile_pic2'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cc',
            name='head',
        ),
        migrations.RemoveField(
            model_name='graphic',
            name='head',
        ),
        migrations.RemoveField(
            model_name='pr',
            name='profile_pic2',
        ),
        migrations.RemoveField(
            model_name='smo',
            name='head',
        ),
        migrations.RemoveField(
            model_name='technical',
            name='profile_pic2',
        ),
        migrations.AddField(
            model_name='gallery',
            name='extra_title',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='gallery',
            name='title',
            field=models.TextField(blank=True, null=True),
        ),
    ]