# Generated by Django 4.2 on 2023-04-15 07:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0008_alter_scoreandtime_cl0tym_alter_scoreandtime_cl1tym_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='users',
            options={'get_latest_by': ['-totalScore'], 'ordering': ['-totalScore']},
        ),
    ]
