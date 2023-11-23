import random
import string


def user_name(size):
    name = ''
    for i in range(size):
        name += ''.join(random.choice(string.ascii_letters))
    return name


def email(size):
    mail = ''
    for i in range(size):
        mail += ''.join(random.choice(string.ascii_letters))
    return f'{mail}@gmail.com'



