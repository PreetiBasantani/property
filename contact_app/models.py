from django.contrib.auth.models import User
from django.db import models
from listings_app.models import Listing
from datetime import datetime

# Create your models here.


class Contact(models.Model):
    listing_id = models.ForeignKey(Listing, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    message = models.TextField(blank=True)
    contact_date = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return str(self.name) + " Listing ID:" + str(self.listing_id)

