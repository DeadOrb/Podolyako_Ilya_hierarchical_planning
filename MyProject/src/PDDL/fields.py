class Predicate:
    def __init__(self):
        self.quantify = ''
        self.name = ''
        self.param_type = []


class Action:
    def __init__(self):
        self.name = ''
        self.parameters = []
        self.quantify_for_precondition = ''
        self.precondition = []
        self.quantify_for_effect = ''
        self.effect = []


class Method:
    def __init__(self):
        self.name = ''
        self.parameters = []
        self.quantify_for_subgoals = ''
        self.subgoals = []
        self.ordering = []
