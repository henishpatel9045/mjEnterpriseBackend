# Generated by Django 4.0.4 on 2022-05-22 04:37

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='about/')),
                ('subtitle', models.CharField(blank=True, max_length=100, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'About Image',
                'ordering': ['-date_created'],
            },
        ),
        migrations.CreateModel(
            name='Offers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('image', models.ImageField(upload_to='offers')),
                ('description', ckeditor.fields.RichTextField()),
                ('link', models.URLField(blank=True, null=True)),
                ('is_listed', models.BooleanField(default=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Offers',
                'ordering': ['last_updated', 'date_created'],
            },
        ),
        migrations.CreateModel(
            name='SiteInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('businessName', models.CharField(default='Mj Enterprise', max_length=100)),
                ('logo', models.ImageField(upload_to='site/')),
                ('aboutUs', ckeditor.fields.RichTextField()),
                ('whatsapp', models.URLField()),
                ('facebook', models.URLField(blank=True, null=True)),
                ('instagram', models.URLField(blank=True, null=True)),
                ('gmail', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=20)),
                ('reg_no', models.CharField(max_length=100)),
                ('gst_in_no', models.CharField(max_length=100)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Site Info',
                'ordering': ['-last_updated'],
            },
        ),
    ]