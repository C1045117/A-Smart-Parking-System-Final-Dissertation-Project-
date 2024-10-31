from django.db import models
from login.models import CustomUser

class Image(models.Model):
    id = models.AutoField(primary_key=True)
    image = models.BinaryField()
    processed_image = models.BinaryField(null=True, blank=True)  # New field for the processed image
    upload_date = models.DateTimeField(auto_now_add=True)
    parking_slot_label = models.TextField()
    availability = models.CharField(max_length=5, default='Red')

class Booking(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    parking_spot = models.ForeignKey(Image, on_delete=models.CASCADE)
    booking_time = models.DateTimeField(auto_now_add=True)
    order_number = models.IntegerField(default=0)
    status = models.CharField(max_length=10, default='Reserved')



