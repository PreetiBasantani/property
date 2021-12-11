from django.db import models
from realtors_app.models import Realtor
from datetime import datetime
# Create your models here.


class Listing(models.Model):
    state_choices=[
                ('ND','North Dakota'),
                ('NE', 'Nebraska'),
                ('NH', 'New Hampshire'),
                ('NJ', 'New Jersey'),
                ('NM', 'New Mexico'),
                ('NV', 'Nevada'),
                ('NY', 'New York'),
                ('OH', 'Ohio'),
                ('OK', 'Oklahoma'),
                ('OR', 'Oregon'),
                ('PA', 'Pennsylvania'),
                ('PR', 'Puerto Rico'),
                ('RI', 'Rhode Island'),
                ('SC', 'South Carolina'),
                ('SD', 'South Dakota'),
                ('TN', 'Tennessee'),
                ('TX', 'Texas'),
                ('UT', 'Utah'),
                ('VA', 'Virginia'),
                ('VI', 'Virgin Islands'),
                ('VT', 'Vermont'),
                ('WA', 'Washington'),
                ('WI', 'Wisconsin'),
                ('WV', 'West Virginia'),
                ('WY', 'Wyoming')
            ]
    price_choices =[
                (100000,'$100,000'),
                (200000,'$200,000'),
                (300000,'$300,000'),
        (400000,'$400,000'),
        (500000,'$500,000'),
        (600000,'$600,000'),
        (700000,'$700,000'),
        (800000,'$800,000'),
        (900000,'$900,000'),
        (1000000,'$1M+'),
    ]

    bedroom_choices=[
        (1,1),
        (2,2),
        (3,3),
        (4,4),
        (5,5),
        (6,6),
        (7,7),
        (8,8),
        (9,9),
        (10,10)

    ]

    realtor = models.ForeignKey(Realtor,on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50,choices=state_choices)
    zipcode = models.SmallIntegerField()
    description = models.TextField(blank=True)
    price = models.IntegerField(choices=price_choices)
    bedrooms = models.IntegerField(choices=bedroom_choices)
    bathrooms= models.DecimalField(max_digits=2,decimal_places=1)
    garage = models.IntegerField(blank=True)
    sq_ft = models.IntegerField()
    lot_size = models.DecimalField(max_digits=5,decimal_places=1)
    photo_main = models.ImageField(upload_to='Photos/%Y/%m/%d', blank=True)
    photo_1 = models.ImageField(upload_to='Photos/%Y/%m/%d', blank=True)
    photo_2 = models.ImageField(upload_to='Photos/%Y/%m/%d', blank=True)
    photo_3 = models.ImageField(upload_to='Photos/%Y/%m/%d', blank=True)
    photo_4 = models.ImageField(upload_to='Photos/%Y/%m/%d', blank=True)
    photo_5 = models.ImageField(upload_to='Photos/%Y/%m/%d', blank=True)
    photo_6 = models.ImageField(upload_to='Photos/%Y/%m/%d', blank=True)
    is_published = models.BooleanField(default=True)
    list_date = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.title

