import datetime
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from multiselectfield import MultiSelectField
from ckeditor.fields import RichTextField

class Car(models.Model):
    STATE_CHOICES = (
        ('AL', 'Alabama'),
        ('AK', 'Alaska'),
        ('AZ', 'Arizona'),
        ('AR', 'Arkansas'),
        ('CA', 'California'),
        ('CO', 'Colorado'),
        ('CT', 'Connecticut'),
        ('DE', 'Delaware'),
        ('DC', 'District Of Columbia'),
        ('FL', 'Florida'),
        ('GA', 'Georgia'),
        ('HI', 'Hawaii'),
        ('ID', 'Idaho'),
        ('IL', 'Illinois'),
        ('IN', 'Indiana'),
        ('IA', 'Iowa'),
        ('KS', 'Kansas'),
        ('KY', 'Kentucky'),
        ('LA', 'Louisiana'),
        ('ME', 'Maine'),
        ('MD', 'Maryland'),
        ('MA', 'Massachusetts'),
        ('MI', 'Michigan'),
        ('MN', 'Minnesota'),
        ('MS', 'Mississippi'),
        ('MO', 'Missouri'),
        ('MT', 'Montana'),
        ('NE', 'Nebraska'),
        ('NV', 'Nevada'),
        ('NH', 'New Hampshire'),
        ('NJ', 'New Jersey'),
        ('NM', 'New Mexico'),
        ('NY', 'New York'),
        ('NC', 'North Carolina'),
        ('ND', 'North Dakota'),
        ('OH', 'Ohio'),
        ('OK', 'Oklahoma'),
        ('OR', 'Oregon'),
        ('PA', 'Pennsylvania'),
        ('RI', 'Rhode Island'),
        ('SC', 'South Carolina'),
        ('SD', 'South Dakota'),
        ('TN', 'Tennessee'),
        ('TX', 'Texas'),
        ('UT', 'Utah'),
        ('VT', 'Vermont'),
        ('VA', 'Virginia'),
        ('WA', 'Washington'),
        ('WV', 'West Virginia'),
        ('WI', 'Wisconsin'),
        ('WY', 'Wyoming'),
    )

    year_choice = []
    THIS_YEAR = datetime.date.today().year
    for year in range(2000, THIS_YEAR + 1):
        year_choice.append(year)

    FEATURES_CHOICES = (
        ('Cruise Control', 'Cruise Control'),
        ('Audio Interface', 'Audio Interface'),
        ('Airbags', 'Airbags'),
        ('Air Conditioning', 'Air Conditioning'),
        ('Seat Heating', 'Seat Heating'),
        ('Alarm System', 'Alarm System'),
        ('ParkAssist', 'ParkAssist'),
        ('Power Steering', 'Power Steering'),
        ('Reversing Camera', 'Reversing Camera'),
        ('Direct Fuel Injection', 'Direct Fuel Injection'),
        ('Auto Start/Stop', 'Auto Start/Stop'),
        ('Wind Deflector', 'Wind Deflector'),
        ('Bluetooth Handset', 'Bluetooth Handset'),
    )

    DOOR_CHOICES = (
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
    )


    title = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length = 2, choices=STATE_CHOICES)
    color = models.CharField(max_length=50)
    model = models.CharField(max_length=255)
    year = models.IntegerField(validators=[MinValueValidator(2000), MaxValueValidator(THIS_YEAR)])
    condition = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=7, decimal_places=2, validators=[MinValueValidator(0)])
    description = RichTextField()
    car_image = models.ImageField(upload_to=f'cars/%Y/%m/%d/')
    car_image_1 = models.ImageField(upload_to=f'cars/%Y/%m/%d/', blank= True)
    car_image_2 = models.ImageField(upload_to=f'cars/%Y/%m/%d/', blank= True)
    car_image_3 = models.ImageField(upload_to=f'cars/%Y/%m/%d/', blank= True)
    car_image_4 = models.ImageField(upload_to=f'cars/%Y/%m/%d/', blank= True)
    features = MultiSelectField(choices=FEATURES_CHOICES, max_length=255)
    body_style = models.CharField(max_length=255)
    engine = models.CharField(max_length=255)
    transmission = models.CharField(max_length=255)
    interior = models.CharField(max_length=255)
    miles = models.IntegerField(validators=[MinValueValidator(0)])
    doors = models.CharField(max_length=1, choices= DOOR_CHOICES, default='4')
    passengers = models.IntegerField(validators=[MinValueValidator(0)])
    vin_no = models.CharField(max_length=255)
    milage = models.IntegerField(validators=[MinValueValidator(0)])
    fuel_type = models.CharField(max_length=255)
    no_of_owners = models.IntegerField(validators=[MinValueValidator(0)])
    is_featured = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)



