from django.core.management.base import BaseCommand
import cv2
import random
from booking.models import Image

class Command(BaseCommand):
    help = 'Initializes the database with images'

    def handle(self, *args, **options):
        # Delete all existing records
        Image.objects.all().delete()
        image1 = cv2.imread('image processing/no car.jpg', cv2.IMREAD_COLOR)
        image2 = cv2.imread('image processing/with car.jpg', cv2.IMREAD_COLOR)

        parking_spots = ['A1', 'A2', 'A3', 'A4', 'A5', 'B1', 'B2', 'B3', 'B4', 'B5']

        # Randomise the image
        for spot in parking_spots:
            img = random.choice([image1, image2])
            is_success, im_buf_arr = cv2.imencode(".jpg", img)
            byte_im = im_buf_arr.tobytes()
            image = Image(image=byte_im, parking_slot_label=spot)
            image.processed_image = None  # Set processed_image to None
            image.save()

        self.stdout.write(self.style.SUCCESS('Successfully initialized images'))


