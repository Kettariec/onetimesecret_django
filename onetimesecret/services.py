import random
import string


def generate_code():
    characters = string.digits + string.ascii_lowercase
    password = ''.join(random.choices(characters, k=10))
    return password
