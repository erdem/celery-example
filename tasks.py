import os
import Image

from celery.task import task
from constants import THUMBNAIL_SIZES, THUMBNAILS_DIRECTORY


@task(name="thumbnail_generater")
def thumbnail_generater(image_path, image_name):
    for thumbnail_size in THUMBNAIL_SIZES:
        thumbnail_folder_name = "%sx%s/" % thumbnail_size
        thumbnail_directory = THUMBNAILS_DIRECTORY + thumbnail_folder_name

        try:
            os.makedirs(thumbnail_directory)
        except OSError:
            pass

        thumbnail_data = {
            "image_name": os.path.splitext(image_name)[0],
            "width": thumbnail_size[0],
            "height": thumbnail_size[1]
        }
        thumbnail_name = "%(image_name)s_%(width)sx%(height)s.jpg" % thumbnail_data
        thumbnail_path = thumbnail_directory + thumbnail_name

        image = Image.open(image_path)
        image.thumbnail(thumbnail_size)
        image.save(thumbnail_path, "JPEG")