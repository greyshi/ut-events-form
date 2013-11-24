import string
import random


def generate_random_string(length, variance=0):
    """Returns a random alphanumeric string of length varying
       by the variance parameter.
    """
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for i in range(random.choice(range(length - variance, length + variance + 1))))
