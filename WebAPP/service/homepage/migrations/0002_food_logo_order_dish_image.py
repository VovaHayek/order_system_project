# Generated by Django 4.0.3 on 2022-09-29 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='food',
            name='logo',
            field=models.ImageField(blank=True, upload_to='logo/'),
        ),
        migrations.AddField(
            model_name='order',
            name='dish_image',
            field=models.ImageField(blank=True, upload_to='dishes/'),
        ),
    ]
