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
        print(self.name)
