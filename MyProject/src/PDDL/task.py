class Task:
    def __init__(self):
        self.name = ''
        self.name_of_domain = ''
        self.objects = []
        self.init = []
        self.quantify_for_goal = ''
        self.goal = []

    def print(self):
        print('name:\n', self.name)

        print('\n\nname_of_domain:\n', self.name_of_domain)

        print('\n\nobjects:\n', *self.objects)

        print('\n\ninit:\n', *self.init)

        print('\n\ngoal:', self.quantify_for_goal, '\n', *self.goal)
