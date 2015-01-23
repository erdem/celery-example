import os

from tasks import thumbnail_generater
from constants import IMAGE_DIRECTORY


def generate_thumbnails():
    images = os.listdir(IMAGE_DIRECTORY)
    for image_name in images:
        image_path = IMAGE_DIRECTORY + image_name
        thumbnail_generater.delay(image_path, image_name)

if __name__ == '__main__':
    generate_thumbnails()