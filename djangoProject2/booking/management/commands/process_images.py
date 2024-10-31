from django.core.management.base import BaseCommand
from booking.models import Image
import cv2
import numpy as np


class Command(BaseCommand):
    help = 'Processes images and updates availability'

    def handle(self, *args, **options):
        net = cv2.dnn.readNet("yolov3 files/yolov3.weights", "yolov3 files/yolov3.cfg")
        layer_names = net.getLayerNames()
        unconnected_out_layers = net.getUnconnectedOutLayers()
        if unconnected_out_layers.ndim == 1:
            unconnected_out_layers = unconnected_out_layers[np.newaxis, :]

        output_layers = [layer_names[i[0] - 1] for i in unconnected_out_layers]

        # Process each image in the database
        for image in Image.objects.all():
            nparr = np.frombuffer(image.image, np.uint8)
            img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

            # resize image
            img = cv2.resize(img, None, fx=0.4, fy=0.4)
            height, width, channels = img.shape

            # object detection
            blob = cv2.dnn.blobFromImage(img, 0.00392, (416, 416), (0, 0, 0), True, crop=False)
            net.setInput(blob)
            outs = net.forward(output_layers)

            car_detected = False
            for out in outs:
                for detection in out:
                    scores = detection[5:]
                    class_id = np.argmax(scores)
                    confidence = scores[class_id]
                    if confidence > 0.5:
                        center_x = int(detection[0] * width)
                        center_y = int(detection[1] * height)
                        w = int(detection[2] * width)
                        h = int(detection[3] * height)
                        x = int(center_x - w / 2)
                        y = int(center_y - h / 2)
                        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

                        car_detected = True
            if car_detected:
                availability = "Red"
            else:
                availability = "Green"
            is_success, im_buf_arr = cv2.imencode(".jpg", img)
            byte_im = im_buf_arr.tobytes()
            image.processed_image = byte_im
            image.availability = availability
            image.save()
        print('Successfully processed images')
