# Generated by Django 5.0 on 2024-03-29 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0007_alter_article_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='visible',
            field=models.BooleanField(default=False),
        ),
    ]
