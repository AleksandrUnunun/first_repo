import random
import string


def rand_list():
    return [random.randint(0, 50) for i in range(30)]

def rand_pass():
    return "".join([random.choice(string.ascii_letters + string.punctuation) for _ in range(8)])

a = rand_list()
print(rand_pass())


