# Generated by Django 2.2.7 on 2019-11-08 03:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('note', '0005_note_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='name',
            new_name='user',
        ),
    ]
