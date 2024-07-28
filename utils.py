import names
from skimage import io, transform

first_name = names.get_first_name()
last_name = names.get_last_name()


def modify_image(image_url):
    image = io.imread(image_url)
    modified_image = transform.rotate(image, 25)
    return modified_image
