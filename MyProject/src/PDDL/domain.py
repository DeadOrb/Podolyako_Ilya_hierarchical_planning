class Domain:
    def __init__(self):
        self.name = ''
        self.requirements = []
        self.types = []
        self.constants = []
        self.predicates = []
        self.actions = []
        self.methods = []

    def print(self):
        print('\nname:')
        print(self.name)

        print('\nrequirements:')
        print(self.requirements)

        print('\ntypes:')
        print(self.types)

        print('\nconstants:')
        print(self.constants)

        print('\npredicates:')
        for predicate in self.predicates:
            predicate.print()

        print('\nActions:')
        for action in self.actions:
            action.print()
            print()