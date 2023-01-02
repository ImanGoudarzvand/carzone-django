# Generated by Django 4.1.4 on 2022-12-26 16:21

import ckeditor.fields
import django.core.validators
from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('state', models.CharField(choices=[('AL', 'Alabama'), ('AK', 'Alaska'), ('AZ', 'Arizona'), ('AR', 'Arkansas'), ('CA', 'California'), ('CO', 'Colorado'), ('CT', 'Connecticut'), ('DE', 'Delaware'), ('DC', 'District Of Columbia'), ('FL', 'Florida'), ('GA', 'Georgia'), ('HI', 'Hawaii'), ('ID', 'Idaho'), ('IL', 'Illinois'), ('IN', 'Indiana'), ('IA', 'Iowa'), ('KS', 'Kansas'), ('KY', 'Kentucky'), ('LA', 'Louisiana'), ('ME', 'Maine'), ('MD', 'Maryland'), ('MA', 'Massachusetts'), ('MI', 'Michigan'), ('MN', 'Minnesota'), ('MS', 'Mississippi'), ('MO', 'Missouri'), ('MT', 'Montana'), ('NE', 'Nebraska'), ('NV', 'Nevada'), ('NH', 'New Hampshire'), ('NJ', 'New Jersey'), ('NM', 'New Mexico'), ('NY', 'New York'), ('NC', 'North Carolina'), ('ND', 'North Dakota'), ('OH', 'Ohio'), ('OK', 'Oklahoma'), ('OR', 'Oregon'), ('PA', 'Pennsylvania'), ('RI', 'Rhode Island'), ('SC', 'South Carolina'), ('SD', 'South Dakota'), ('TN', 'Tennessee'), ('TX', 'Texas'), ('UT', 'Utah'), ('VT', 'Vermont'), ('VA', 'Virginia'), ('WA', 'Washington'), ('WV', 'West Virginia'), ('WI', 'Wisconsin'), ('WY', 'Wyoming')], max_length=2)),
                ('color', models.CharField(max_length=50)),
                ('model', models.CharField(max_length=255)),
                ('year', models.IntegerField(validators=[django.core.validators.MinValueValidator(2000), django.core.validators.MaxValueValidator(2022)])),
                ('condition', models.CharField(max_length=255)),
                ('price', models.DecimalField(decimal_places=2, max_digits=7)),
                ('description', ckeditor.fields.RichTextField()),
                ('car_image', models.ImageField(upload_to='cars/<django.db.models.fields.CharField>/')),
                ('car_image_1', models.ImageField(blank=True, upload_to='cars/<django.db.models.fields.CharField>/')),
                ('car_image_2', models.ImageField(blank=True, upload_to='cars/<django.db.models.fields.CharField>/')),
                ('car_image_3', models.ImageField(blank=True, upload_to='cars/<django.db.models.fields.CharField>/')),
                ('car_image_4', models.ImageField(blank=True, upload_to='cars/<django.db.models.fields.CharField>/')),
                ('features', multiselectfield.db.fields.MultiSelectField(choices=[('Cruise Control', 'Cruise Control'), ('Audio Interface', 'Audio Interface'), ('Airbags', 'Airbags'), ('Air Conditioning', 'Air Conditioning'), ('Seat Heating', 'Seat Heating'), ('Alarm System', 'Alarm System'), ('ParkAssist', 'ParkAssist'), ('Power Steering', 'Power Steering'), ('Reversing Camera', 'Reversing Camera'), ('Direct Fuel Injection', 'Direct Fuel Injection'), ('Auto Start/Stop', 'Auto Start/Stop'), ('Wind Deflector', 'Wind Deflector'), ('Bluetooth Handset', 'Bluetooth Handset')], max_length=50)),
                ('body_style', models.CharField(max_length=255)),
                ('engine', models.CharField(max_length=255)),
                ('transmission', models.CharField(max_length=255)),
                ('interior', models.CharField(max_length=255)),
                ('miles', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)])),
                ('doors', models.CharField(choices=[('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6')], default='4', max_length=1)),
                ('passengers', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)])),
                ('vin_no', models.CharField(max_length=255)),
                ('milage', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)])),
                ('fuel_type', models.CharField(max_length=255)),
                ('no_of_owners', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)])),
                ('is_featured', models.BooleanField(default=False)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]