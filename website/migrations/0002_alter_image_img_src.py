# Generated by Django 4.0.5 on 2022-07-07 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='img_src',
            field=models.FileField(upload_to='slider_images'),
        ),
    ]
