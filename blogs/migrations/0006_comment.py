# Generated by Django 5.0.4 on 2024-04-26 12:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0005_remove_blog_categories_blog_categories'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('commented_by', models.CharField(blank=True, max_length=10, null=True)),
                ('commented_content', models.CharField(max_length=100)),
                ('blog', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='blogs.blog')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
