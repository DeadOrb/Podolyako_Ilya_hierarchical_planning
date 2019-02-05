import logging


def take_part(file):
    first = file.find('(')
    right_parentheses = 1
    for i in range(first + 1, len(file)):
        if file[i] == '(':
            right_parentheses += 1
        if file[i] == ')':
            right_parentheses -= 1
        if right_parentheses < 0:
            logging.error("Некорректные входные данные!")
        if right_parentheses == 0:
            return file[first + 1: i]


def delete_part(file):
    first = file.find('(')
    right_parentheses = 1
    for i in range(first + 1, len(file)):

        if file[i] == '(':
            right_parentheses += 1

        if file[i] == ')':
            right_parentheses -= 1

        if right_parentheses < 0:
            logging.error("Некорректные входные данные!")

        if right_parentheses == 0:
            return file[:first] + file[i + 1:]


def take_line(file):
    end_of_part = file.find('\n')
    return file[:end_of_part]

def delete_line(file):
    new_begin = file.find('\n')
    return file[new_begin:]
