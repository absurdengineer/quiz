# Generated by Django 4.1.3 on 2022-12-03 20:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_quiz_options'),
    ]

    operations = [
        migrations.RenameField(
            model_name='answer',
            old_name='answer',
            new_name='title',
        ),
        migrations.RenameField(
            model_name='question',
            old_name='question',
            new_name='title',
        ),
        migrations.RenameField(
            model_name='quiz',
            old_name='name',
            new_name='title',
        ),
    ]