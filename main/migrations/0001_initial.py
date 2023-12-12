# Generated by Django 4.2.7 on 2023-11-30 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EventList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=264)),
                ('images', models.ImageField(upload_to='event_images')),
                ('description', models.TextField()),
                ('event_date', models.CharField(blank=True, max_length=50)),
                ('slug', models.SlugField(blank=True, unique=True)),
            ],
        ),
    ]
