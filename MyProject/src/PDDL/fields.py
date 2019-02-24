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
    def __init__(self, text=None, domain=None):
        if text is None and domain is None:
            self.name = ''
            self.parameters = []
            self.quantify_for_precondition = ''
            self.precondition = []
            self.quantify_for_effect = ''
            self.effect = []
        else:

            self.name = ''
            self.parameters = []
            self.quantify_for_precondition = ''
            self.precondition = []
            self.quantify_for_effect = ''
            self.effect = []

            self.name = re.sub(r':action ', '', re.search(r':action [\w, -]+', text).group(0))

            parameters = parser.take_part(text)
            parameters = re.findall(r'\?\w+ - \w+', parameters)
            for param in parameters:
                self.parameters.append([param.split()[0], param.split()[-1]])
            text = parser.delete_part(text)

            precondition = parser.take_part(text)
            quantify = re.search(r':precondition\s\(and', text)
            if quantify is not None:
                if quantify.group(0).find('and') != -1:
                    self.quantify_for_precondition = 'and'
                else:
                    self.quantify_for_precondition = 'or'
            else:
                precondition = '(' + precondition + ')'
            while precondition.find(')') != -1:
                predicate = parser.take_part(precondition)
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
                precondition = parser.delete_part(precondition)
            text = parser.delete_part(text)

            if text.find('and') != -1:
                self.quantify_for_effect = 'and'
                text = parser.take_part(text)
            elif text.find('or') != -1:
                self.quantify_for_effect = 'or'
                text = parser.take_part(text)
            while text.find('(') != -1:
                positivity = True
                predicate = parser.take_part(text)
                if predicate.find('not') != -1:
                    positivity = False
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
                if positivity:
                    self.effect.append(Predicate.make_predicate(actual_predicate, predicate_param))
                else:
                    self.effect.append('(not ' + Predicate.make_predicate(actual_predicate, predicate_param) + ')')
                text = parser.delete_part(text)

    def print(self):
        print('name:', self.name, '\n')
        print('parameters:', *self.parameters, '\n')
        print('precondition:', self.quantify_for_precondition)
        for predicate in self.precondition:
            print(predicate)
        print('')
        print('effect:', self.quantify_for_effect)
        for predicate in self.effect:
            print(predicate)

    def action_for_method(self, parameters):
        # TODO: возможно добавить проверку на совместимость типов
        effect = []
        precondition = []
        conformity_parameters = []
        for i in range(len(parameters)):
            conformity_parameters.append([self.parameters[i][0], '$' + str(i) + '$'])
        for i in self.effect:
            eff = i
            for j in range(len(conformity_parameters)):
                eff = (eff.replace(conformity_parameters[j][0], conformity_parameters[j][1]))
            effect.append(eff)
        for i in range(len(effect)):
            for j in range(len(parameters)):
                effect[i] = effect[i].replace(conformity_parameters[j][1], parameters[j])

        for i in self.precondition:
            pre = i
            for j in range(len(conformity_parameters)):
                pre = (pre.replace(conformity_parameters[j][0], conformity_parameters[j][1]))
            precondition.append(pre)
        for i in range(len(precondition)):
            for j in range(len(parameters)):
                precondition[i] = precondition[i].replace(conformity_parameters[j][1], parameters[j])

        return precondition, effect
