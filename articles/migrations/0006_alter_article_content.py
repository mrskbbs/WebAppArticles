# Generated by Django 5.0 on 2024-03-29 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0005_alter_article_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='content',
            field=models.JSONField(default={'blocks': [[{'content': '', 'type': 'h1'}]]}),
        ),
    ]
