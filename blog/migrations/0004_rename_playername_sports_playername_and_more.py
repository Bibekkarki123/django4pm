# Generated by Django 5.0.6 on 2024-05-20 11:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_sports'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sports',
            old_name='PlayerName',
            new_name='Playername',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='Address',
            new_name='address',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='Name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='teacher',
            old_name='Address',
            new_name='address',
        ),
        migrations.RenameField(
            model_name='teacher',
            old_name='Name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='teacher',
            old_name='Subject',
            new_name='subject',
        ),
    ]
