import random

nouns = tuple(open('blindr/data/nouns.txt', 'r'))
adjectives = tuple(open('blindr/data/adjectives.txt', 'r'))

def generate_name():
    noun = random.choice(nouns).strip()
    adjective = random.choice(adjectives).strip()

    return '{} {}'.format(adjective.capitalize(), noun.capitalize())
