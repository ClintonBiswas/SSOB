# Generated by Django 4.2.7 on 2023-12-03 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_teammembers'),
    ]

    operations = [
        migrations.AddField(
            model_name='teammembers',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to='team_members'),
        ),
    ]
