import random


def rand_list():
    return [random.randint(0, 50) for i in range(30)]


print(rand_list())
print(rand_list())