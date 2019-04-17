import csv
import string
import random

alphabet = string.ascii_lowercase
wovel = "aeiouy"
consonant = "bcdfghjklmnpqrstvwxyz"
table = []
for i in range(0, len(alphabet)):
    table.append([])
    for j in range(0, len(alphabet)):
        table[i].append(0)


def is_wovel(letter):
    return letter.lower() in wovel


def name_generator(n: int, table) -> str:
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
            if total != 0:
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


def get_letter_index(letter):
    for i in range(0, len(alphabet)):
        if letter == alphabet[i]:
            return i


def gen_matrix_from_name_list(name_list):
    """
    Reads lines with names from file. Must be 1 name in a row
    Generates matrix of possibilities for letters in names,
    normalize and return it as a list of lists
    :param name_list: srt
    :return: list
    """
    with open(name_list, "r") as file:
        f = file.readlines()
        for name in f:
            for i in range(0, len(name) - 2):
                letter1 = name[i].lower()
                letter2 = name[i+1].lower()
                index1 = get_letter_index(letter1)
                index2 = get_letter_index(letter2)
                table[index1][index2] += 1
    return normalize_matrix(table)


def matrix_to_file(file, table):
    """
    Writes table to file.
    You can ues Exel to open it and see nice table of probabilities
    :param file: str
    :param table: list
    :return: None
    """
    with open(file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
        for i in range(0, len(alphabet)):
            writer.writerow(table[i])


def read_table_from_csv(file):
    """
    Reads table of probabilities from a file
    Return list of lists
    :param file: str
    :return: list
    """
    new_table = []
    with open(file, 'r') as f:
        lines = f.readlines()
        for line in lines:
            # convert comma-separated string into list of float values
            new_table.append(list(map(lambda x: float(x), line.split(','))))
    return new_table

f = "./resources/human_female.csv"
l = "./resources/girls_names.csv"
# girls = gen_matrix_from_name_list(l)
# matrix_to_file(f, girls)
nt = read_table_from_csv(f)

for i in range(10):
    print(name_generator(random.choice(range(3, 9)), nt))