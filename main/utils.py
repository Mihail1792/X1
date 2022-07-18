import string
import random


def create_random_code():
    """Генерирует случайный код"""
    length = 6
    char = string.ascii_letters + string.digits
    return ''.join(random.choice(char) for x in range(length))
