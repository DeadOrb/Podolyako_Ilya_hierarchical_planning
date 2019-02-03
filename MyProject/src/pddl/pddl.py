#It is part of project in Higher School of Economics on FCS
#
#That project of planner:
#This class implements the storage of the pddl language object.



class Domain:
    def __init__(self, name, types, predicates, actions, constants={}):
        """
        name: The name of the domain
        types: A dict of typename->Type instances in the domain
        predicates: A list of predicates in the domain
        actions: A list of actions in the domain
        constants: A dict of name->type pairs of the constants in the domain
        """
        self.name = name
        self.types = types
        self.predicates = predicates
        self.actions = actions
        self.constants = constants

    def __repr__(self):
        return ('< Domain definition: %s Predicates: %s Actions: %s '
                'Constants: %s >' % (self.name,
                                     [str(p) for p in self.predicates],
                                     [str(a) for a in self.actions],
                                     [str(c) for c in self.constants]))
    __str__ = __repr__

class Problem:
    def __init__(self, name, domain, objects, init, goal):
        """
        name: The name of the problem
        domain: The domain in which the problem has to be solved
        objects: A dict name->type of objects that are used in the problem
        init: A list of predicates describing the initial state
        goal: A list of predicates describing the goal state
        """
        self.name = name
        self.domain = domain
        self.objects = objects
        self.initial_state = init
        self.goal = goal

    def __repr__(self):
        return ('< Problem definition: %s '
                'Domain: %s Objects: %s Initial State: %s Goal State : %s >' %
                (self.name, self.domain.name,
                 [self.objects[o].name for o in self.objects],
                 [str(p) for p in self.initial_state],
                 [str(p) for p in self.goal]))

    __str__ = __repr__