#


class Domain:
    def __init__(self):
        self.name = ''
        self.requirements = []
        self.types = set()
        self.predicates = set()
        self.actions = set()
        self.methods = set()

    def print(self):
        print(self.name)
        print(*self.requirements)
        print(*self.types)
        print(self.predicates)
        for i in self.actions:
            i.print()
        for i in self.methods:
            i.print()
