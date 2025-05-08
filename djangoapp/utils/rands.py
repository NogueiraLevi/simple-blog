from random import SystemRandom
import string

from django.utils.text import slugify

def random_letter(k=5):
    return ''.join(SystemRandom().choices(
        string.ascii_letters + string.digits,
        k=k
    ))


def slugfy_new(text):
    return slugify(text) + '-' + random_letter
