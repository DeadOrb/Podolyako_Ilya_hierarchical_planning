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


class Predicate:
    def __init__(self, data):
        self.name = ''
        self.quantify = ''
        self.params = []

        if data.find("and ") != -1 or \
                data.find("or ") != -1 or \
                data.find("not ") != -1 or \
                data.find("exists ") != -1 \
                or data.find("forall ") != -1:

            self.quantify = data.split()[0]
            data = take_part(data)

        formal_view = data.split()
        self.name = formal_view[0]
        for i in range(1, len(formal_view)):

            if formal_view[i].find('?') != -1:
                self.params.append(formal_view[i])

            if formal_view[i] == '-':
                self.params[-1] = (self.params[-1], formal_view[i + 1])
