import random
import string


def random_string(maxlen):
    length = random.randrange(maxlen)
    symbols = (string.ascii_letters + string.digits +
               string.punctuation + " "*10)
    result = ''.join([random.choice(symbols) for _ in range(length)])
    return result
