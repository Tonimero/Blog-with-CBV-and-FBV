# Generated by Django 4.1.1 on 2022-09-25 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('g_blog_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='categorypage',
            name='name',
            field=models.CharField(default='Select a category', max_length=300),
        ),
        migrations.AddField(
            model_name='categorypage',
            name='slug',
            field=models.SlugField(default=True),
        ),
    ]
