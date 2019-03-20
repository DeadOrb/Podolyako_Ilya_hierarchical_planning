#

# TODO: у методов проблема с началом и целью


class Method:
    def __init__(self):
        self.name = ''
        self.parameters = []
        self.quantifier_for_subgoals = 'and'
        self.subgoals = []
        self.quantifier_for_ordering = 'and'
        self.ordering = []
        self.init = []
        self.goal = []
        self.level = 0

    def print(self):
        print(self.name)
        for i in self.parameters:
            i.print()
        print(self.quantifier_for_subgoals)
        for i in self.subgoals:
            i.print()
        print(self.quantifier_for_ordering)
        for i in self.ordering:
            i.print()
        print('level:', self.level)


class Action:
    def __init__(self):
        self.name = ''
        self.parameters = []
        self.quantifier_for_precondition = 'and'
        self.precondition = []
        self.quantifier_for_effect = 'and'
        self.effect = []
        self.level = 0

    def print(self):
        print(self.name)
        for i in self.parameters:
            i.print()
        print(self.quantifier_for_precondition)
        for i in self.precondition:
            i.print()
        print(self.quantifier_for_effect)
        for i in self.effect:
            i.print()
        print('level:', self.level)

    # def checker_for_using(self):

    # def use_action(self, parameters):


# class Environment:
#     def __init__(self):
#         self.


class Predicate:
    def __init__(self):
        self.name = ''
        self.parameters = []
        self.positively = True

    def __eq__(self, other):
        return self.name == other.name \
               and self.positively == other.positively \
               and self.parameters == other.parameters

    def print(self):
        if not self.positively:
            print('not', self.name, *self.parameters)
        else:
            print(self.name, *self.parameters)


class Parameter:
    def __init__(self):
        self.name = ''
        self.type = ''

    def __eq__(self, other):
        return self.type == other.type

    def print(self):
        print(self.name, self.type)


class Task:
    def __init__(self):
        self.name = ''
        self.parameters = []
        self.action = Action()

    def print(self):
        print(self.name)
        print(*self.parameters)
        self.action.print()


class Order:
    def __init__(self):
        self.first = ''
        self.second = ''

    def print(self):
        print(self.first)
        print(self.second)
