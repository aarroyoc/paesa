import random

def get_generic_phrase():
    with open("text/generic_text.txt") as f:
        return random.choice(f.readlines())