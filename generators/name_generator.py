import string
import random

alphabet = string.ascii_lowercase
wovel = "aeiouy"
consonant = "bcdfghjklmnpqrstvwxyz"
table = []
for i in range(0, len(alphabet)):
    table.append([])
    for j in range(0, len(alphabet)):
        table[i].append(1)


def is_wovel(letter):
    return letter.lower() in wovel


def name_generator(n: int) -> str:
    name1 = random.choice(alphabet).upper()  # 1st letter - random uppercase letter

    for i in range(1, n):
        letter = pick_letter(i-1, normalize_matrix(table))

        if is_wovel(name1[i - 1]) and is_wovel(name1[i - 2]):
            while is_wovel(letter):
                letter = pick_letter(i - 1, table)
            name1 += letter
        elif not is_wovel(name1[i - 1]) and not is_wovel(name1[i - 2]):
            while not is_wovel(letter):
                letter = pick_letter(i - 1, table)
            name1 += letter
        else:
            name1 += letter

    return name1


def normalize_matrix(table):
    """
    Counts % chance of every letter goes after every letter in alphabet
    :param table: list of lists
    :return: list of lists
    """
    for i in range(0, len(table)):
        total = 0
        for j in range(0, len(table)):
            total += table[i][j]
        for j in range(0, len(table)):
            table[i][j] /= total
    return table


def pick_letter(letter: int, table: list) -> str:
    """
    Takes a letter by index from table and returns char
    based on % this char can follow the letter
    :param letter: int
    :param table: list of lists
    :return: char
    """
    r = random.random()  # random float from 0 to 1
    total = 0
    for i in range(0, len(table)):
        total += table[letter][i]  # increments total by float value of next char
        if r <= total or i == len(table):
            return alphabet[i]


name = name_generator(5)
print(name)