# Generated by Django 4.2.7 on 2024-06-06 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0019_alter_eventlist_options_eventlist_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventlist',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]