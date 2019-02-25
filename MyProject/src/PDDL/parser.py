import re
import logging


# TODO: сделать парсер

class ParserForDomain:
    def __init__(self, domain):
        self.name = ''
        self.requirements = ''
        self.types = ''
        self.constants = ''
        self.predicates = ''
        self.actions = []
        self.methods = []

        domain = take_part(domain)

        self.name = take_part(domain)
        domain = delete_part(domain)

        if domain.find(':requirements') != -1:
            self.requirements = take_part(domain)
            domain = delete_part(domain)

        if domain.find(':types') != -1:
            self.types = take_part(domain)
            domain = delete_part(domain)

        if domain.find(':constants') != -1:
            self.constants = take_part(domain)
            domain = delete_part(domain)

        if domain.find(':predicates') != -1:
            self.predicates = take_part(domain)
            domain = delete_part(domain)

        while domain.find(':action') != -1:
            self.actions.append(take_part(domain))
            domain = delete_part(domain)

        while domain.find(':method') != -1:
            self.methods.append(take_part(domain))
            domain = delete_part(domain)

    def print(self):
        print(self.name)
        print('********************************************************************************************')

        print(self.requirements)
        print('********************************************************************************************')

        print(self.types)
        print('********************************************************************************************')

        print(self.constants)
        print('********************************************************************************************')

        print(self.predicates)
        print('********************************************************************************************')

        for action in self.actions:
            print(action)
            print('********************************************************************************************')

        for method in self.methods:
            print(method)
            print('********************************************************************************************')

class ParserForTask:
    def __init__(self, text_task):
        self.name = ''
        self.name_of_domain = ''
        self.objects = ''
        self.init = ''
        self.goal = ''

        text_task = take_part(text_task)

        self.name = take_part(text_task)
        text_task = delete_part(text_task)

        self.name_of_domain = take_part(text_task)
        text_task = delete_part(text_task)

        self.objects = take_part(text_task)
        text_task = delete_part(text_task)

        self.init = take_part(text_task)
        text_task = delete_part(text_task)

        self.goal = take_part(text_task)

    def print(self):
        print(self.name)
        print('********************************************************************************************')

        print(self.name_of_domain)
        print('********************************************************************************************')

        print(self.objects)
        print('********************************************************************************************')

        print(self.init)
        print('********************************************************************************************')

        print(self.goal)


def take_part(file):
    first = file.find('(')
    if first == -1:
        return ' '
    right_parentheses = 1
    for i in range(first + 1, len(file)):

        if file[i] == '(':
            right_parentheses += 1

        if file[i] == ')':
            right_parentheses -= 1

        if right_parentheses < 0:
            logging.error("Некорректные входные данные, ошибка в расстановке скобок.")

        if right_parentheses == 0:
            return file[first + 1: i]


def delete_part(file):
    first = file.find('(')
    if first == -1:
        return ' '
    right_parentheses = 1
    for i in range(first + 1, len(file)):

        if file[i] == '(':
            right_parentheses += 1

        if file[i] == ')':
            right_parentheses -= 1

        if right_parentheses < 0:
            logging.error("Некорректные входные данные, ошибка в расстановке скобок.")

        if right_parentheses == 0:
            return file[:first] + file[i + 1:]
