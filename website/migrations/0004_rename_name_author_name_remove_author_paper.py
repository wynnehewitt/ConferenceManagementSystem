# Generated by Django 4.1.2 on 2022-10-30 02:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_author_paper'),
    ]

    operations = [
        migrations.RenameField(
            model_name='author',
            old_name='Name',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='author',
            name='Paper',
        ),
    ]