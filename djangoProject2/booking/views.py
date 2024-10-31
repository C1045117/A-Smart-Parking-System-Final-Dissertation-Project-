from django.shortcuts import render, get_object_or_404, redirect
from .models import Image, Booking
import base64
from django.contrib.auth.decorators import login_required

@login_required
def confirmed_bookings(request):
    confirmed_bookings = Booking.objects.filter(user=request.user)
    return render(request, 'confirmed_bookings.html', {'bookings': confirmed_bookings})

def parking_reservation(request):
    # get all image
    images = Image.objects.all()
    parking_spots = {image.parking_slot_label: image.availability for image in images}

    return render(request, 'booking.html', {'parking_spots': parking_spots})

def parking_spot(request, parking_spot_label):
    image = get_object_or_404(Image, parking_slot_label=parking_spot_label)
    processed_image_base64 = base64.b64encode(image.processed_image).decode('utf-8')
    processed_image_data_url = 'data:image/jpeg;base64,' + processed_image_base64
    availability = request.session.get(f'parking_spot_{parking_spot_label}_availability', 'Green')
    return render(request, 'parking_spot.html', {'image': processed_image_data_url, 'label': image.parking_slot_label, 'availability' : availability})


from django.utils import timezone
import random

def booking_confirmation(request, order_number):
    booking = get_object_or_404(Booking, order_number=order_number)
    return render(request, 'booking_confirmation.html', {'booking': booking})


def create_booking(request, parking_spot_label):
    image = get_object_or_404(Image, parking_slot_label=parking_spot_label)
    if image.availability == 'Red':
        return render(request, 'error.html', {'message': 'This spot is already booked.'})

    order_number = random.randint(100000, 999999)

    # new booking
    booking = Booking(user=request.user, parking_spot=image, booking_time=timezone.now(), order_number=order_number)
    booking.save()
    image.availability = 'Red'
    image.save()
    return redirect('booking_confirmation', order_number=order_number)
