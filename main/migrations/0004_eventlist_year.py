# Generated by Django 4.2.7 on 2023-12-01 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_eventlist_schedule'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventlist',
            name='year',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
