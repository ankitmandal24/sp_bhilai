# Generated by Django 3.2.12 on 2022-08-19 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0015_auto_20220805_2002'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True)),
                ('role', models.CharField(max_length=200, null=True)),
                ('profile_pic', models.ImageField(blank=True, null=True, upload_to='')),
                ('twitter', models.CharField(blank=True, max_length=500, null=True)),
                ('linkedin', models.CharField(blank=True, max_length=500, null=True)),
                ('instagram', models.CharField(blank=True, max_length=500, null=True)),
            ],
        ),
    ]
