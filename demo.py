import os

from tasks import thumbnail_generator
from constants import IMAGE_DIRECTORY, IMAGE_EXTENSIONS


def generate_thumbnails():
    files = os.listdir(IMAGE_DIRECTORY)
    for file in files:
        file_name, file_extension = os.path.splitext(file)
        if file_extension in IMAGE_EXTENSIONS:
            image_path = os.path.join(IMAGE_DIRECTORY, file_name)
            thumbnail_generator.delay(image_path, file_name)

if __name__ == '__main__':
    generate_thumbnails()

