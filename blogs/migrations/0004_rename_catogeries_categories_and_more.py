# Generated by Django 5.0.4 on 2024-04-26 10:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0003_blog_catogeries'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Catogeries',
            new_name='Categories',
        ),
        migrations.RenameField(
            model_name='blog',
            old_name='catogeries',
            new_name='categories',
        ),
    ]