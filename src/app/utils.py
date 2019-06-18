import os
import random
import string

async def cleanup(path):
    os.remove(path)


async def random_string(length: int =10):
    return ''.join([random.choice(string.ascii_letters) for n in range(length)])
