# Generated by Django 4.1.1 on 2022-09-25 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('g_blog_app', '0002_categorypage_name_categorypage_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categorypage',
            name='name',
            field=models.CharField(default=False, max_length=300),
        ),
        migrations.AlterField(
            model_name='categorypage',
            name='slug',
            field=models.SlugField(default=False),
        ),
    ]
