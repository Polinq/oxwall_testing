import random
import string

utf_symbols = ''.join([chr(l) for l in range(1, 0x10ffff)
                       if chr(l).isprintable()])

cyr_symbol = ''.join([chr(l) for l in range(0x0400, 0x04FF)
                      if chr(l).isprintable()])


def random_string(maxlen, cyrillic=False, all_utf8=False):
    length = random.randrange(maxlen)
    if all_utf8:
        symbols = utf_symbols
    else:
        symbols = (string.ascii_letters + string.digits +
                   string.punctuation + " "*10)
        if cyrillic:
            symbols += cyr_symbol
    result = ''.join([random.choice(symbols) for _ in range(length)])
    return result
