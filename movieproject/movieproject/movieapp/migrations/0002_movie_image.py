# Generated by Django 4.1.3 on 2023-05-23 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='image',
            field=models.ImageField(default='hello', upload_to='gallery'),
            preserve_default=False,
        ),
    ]
