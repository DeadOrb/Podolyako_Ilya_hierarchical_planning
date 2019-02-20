import src.PDDL.parser as parser
import re
import logging


class Predicate:
    def __init__(self, text):
        self.positively = True
        self.name = ''
        self.param_type = []

        if text.find('not') != -1:
            self.positively = False
            text = parser.take_part(text)

        self.name = re.search(r'\w+', text).group(0)
        objects = re.findall(r'\?\w+ - \w+', text)
        for type in objects:
            self.param_type.append(type.split()[-1])

    def print(self):

        if not self.positively:
            print("not", end='')

        print(self.name, *self.param_type)

    def make_predicate(self, param):
        new_predicate = '('
        for i in self.param_type:
            for j in param:
                if i != j[1]:
                    logging.error("Неправильно определенные действия или не хватате предикатов!")
        new_predicate += self.name
        for i in param:
            new_predicate += ' '
            new_predicate += i[0]
        new_predicate += ')'
        return new_predicate

class Action:
    def __init__(self, text, domain):
        self.name = ''
        self.parameters = []
        self.quantify_for_precondition = ''
        self.precondition = []
        self.quantify_for_effect = ''
        self.effect = []

        self.name = re.sub(r':action ', '', re.search(r':action \w+', text).group(0))

        parameters = parser.take_part(text)
        parameters = re.findall(r'\?\w+ - \w+', parameters)
        for param in parameters:
            self.parameters.append([param.split()[0], param.split()[-1]])
        text = parser.delete_part(text)

        precondition = parser.take_part(text)
        if precondition.find('and') != -1:
            self.quantify_for_precondition = 'and'
        if precondition.find('or') != -1:
            self.quantify_for_precondition = 'or'
        predicate = precondition
        print(predicate)
        #TODO: изменить, проблема с предикатами без скобок и с остальными предикатами
        while predicate.find(')') != -1:
            predicate = parser.take_part(predicate)
            name_predicate = re.search(r'\w+', predicate).group(0)
            param = re.findall(r'\?\w+', predicate)
            predicate_param = []
            for i in param:
                for j in self.parameters:
                    if j[0] == i:
                        predicate_param.append(j)
            for i in domain.predicates:
                if i.name == name_predicate:
                    actual_predicate = i
            self.precondition.append(Predicate.make_predicate(actual_predicate, predicate_param))
            predicate = parser.delete_part(predicate)

        text = parser.delete_part(text)


    def print(self):
        print('name:', self.name)
        print('parameters:', *self.parameters)
        print('precondition:', '\n', self.quantify_for_precondition)
        for predicate in self.precondition:
            print(predicate)


class Method:
    def __init__(self):
        self.name = ''
        self.parameters = []
        self.quantify_for_subgoals = ''
        self.subgoals = []
        self.ordering = []
