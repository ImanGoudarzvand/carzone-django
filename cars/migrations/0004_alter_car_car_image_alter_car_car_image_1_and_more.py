# Generated by Django 4.1.4 on 2022-12-27 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0003_alter_car_features'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='car_image',
            field=models.ImageField(upload_to='cars/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='car',
            name='car_image_1',
            field=models.ImageField(blank=True, upload_to='cars/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='car',
            name='car_image_2',
            field=models.ImageField(blank=True, upload_to='cars/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='car',
            name='car_image_3',
            field=models.ImageField(blank=True, upload_to='cars/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='car',
            name='car_image_4',
            field=models.ImageField(blank=True, upload_to='cars/%Y/%m/%d/'),
        ),
    ]
