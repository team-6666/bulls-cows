import random

def generateNum():
    while True:
        num = random.randint(1000,9999)
        if noDuplicates(num):
            return num
