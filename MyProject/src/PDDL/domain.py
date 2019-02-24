class Domain:
    def __init__(self):
        self.name = ''
        self.requirements = []
        self.types = []
        self.constants = []
        self.predicates = []
        self.actions = []

    def print(self):
        print('\n\nname:')
        print(self.name)

        print('\n\nrequirements:')
        print(self.requirements)

        print('\n\ntypes:')
        print(self.types)

        print('\n\nconstants:')
        print(self.constants)

        print('\n\npredicates:')
        for predicate in self.predicates:
            predicate.print()

        print('\n\nActions:\n')
        for action in self.actions:
            action.print()
            print('')
