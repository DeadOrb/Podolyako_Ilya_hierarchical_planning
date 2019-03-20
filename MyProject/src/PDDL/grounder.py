#
import src.PDDL.fields as fields
import src.PDDL.parser as parser


class GrounderForDomain:
    def __init__(self, file, domain):
        domain.name = file.name.split()[1]

        domain.requirements = file.requirements.split()[1:]

        domain.types = set(file.types.split()[1:])

        predicates = file.predicates
        while predicates.find('(') != -1:
            domain.predicates.add(parser.take_part(predicates))
            predicates = parser.delete_part(predicates)

        actions = file.actions
        for i in actions:
            domain.actions.add(make_action(i))

        methods = file.methods
        for i in methods:
            if i[1] != 1:
                domain.methods.add(make_method(domain, methods, i))


class GrounderForTask:
    def __init__(self, file, task):
        task.name = file.name.split()[1]
        task.domain = file.name_of_domain.split()[1]
        task.objects = []

        objects = file.objects.split()[1:]

        for i in range(len(objects)):
            if objects[i] == '-':
                param = fields.Parameter()
                param.name = objects[i-1]
                param.type = objects[i+1]
                task.objects.append(param)

        task.init = set()
        text_init = file.init

        while text_init.find('(') != -1:
            predicate = parser.take_part(text_init)
            task.init.add('(' + predicate + ')')
            text_init = parser.delete_part(text_init)

        task.goal = set()
        text_goal = file.goal

        while text_goal.find('(') != -1:
            predicate = parser.take_part(text_goal)
            task.goal.add('(' + predicate + ')')
            text_goal = parser.delete_part(text_goal)


def make_method(domain, methods, pair_method):
    pair_method[1] = 1
    method = pair_method[0]
    new_method = fields.Method()
    new_method.name = method.split()[1]

    parameters = parser.take_part(method).split()
    for i in range(len(parameters)):
        if parameters[i] == '-':
            parameter = fields.Parameter()
            parameter.name = parameters[i - 1]
            parameter.type = parameters[i + 1]
            new_method.parameters.append(parameter)

    method = parser.delete_part(method)

    text_subgoals = parser.take_part(method)
    method = parser.delete_part(method)

    if text_subgoals.find('(and ') != -1:
        new_method.quantifier_for_subgoals = 'and'
    elif text_subgoals.find('(or ') != -1:
        new_method.quantifier_for_subgoals = 'or'
    while text_subgoals.find('(') != -1:
        text_task = parser.take_part(text_subgoals)
        new_task = fields.Task()
        new_task.name = text_task.split()[0]
        text_task = parser.take_part(text_task)
        # print(text_task)
        new_task.action, new_task.parameters = find_action(domain, text_task.split()[0], methods), text_task.split()[1:]
        new_method.subgoals.append(new_task)
        text_subgoals = parser.delete_part(text_subgoals)
        if new_method.level <= new_task.action.level:
            new_method.level = new_task.action.level + 1

    text_ordering = parser.take_part(method)
    method = parser.delete_part(method)

    if text_ordering.find('(and ') != -1:
        new_method.quantifier_for_ordering = 'and'
    elif text_ordering.find('(or ') != -1:
        new_method.quantifier_for_ordering = 'or'

    while text_ordering.find('(') != -1:
        new_order = fields.Order()
        text_order = parser.take_part(text_ordering).split()
        text_ordering = parser.delete_part(text_ordering)
        new_order.first = text_order[0]
        new_order.second = text_order[2]
        new_method.ordering.append(new_order)

    return new_method


def make_action(text):
    action = fields.Action()

    action.name = text.split()[1]

    parameters = parser.take_part(text).split()
    for i in range(len(parameters)):
        if parameters[i] == '-':
            parameter = fields.Parameter()
            parameter.name = parameters[i - 1]
            parameter.type = parameters[i + 1]
            action.parameters.append(parameter)
    text = parser.delete_part(text)

    precondition = parser.take_part(text)
    text = parser.delete_part(text)
    if precondition.find('(and ') != -1:
        action.quantifier_for_precondition = 'and'
        precondition = parser.take_part(precondition)
    elif precondition.find('(or ') != -1:
        action.quantifier_for_precondition = 'or'
        precondition = parser.take_part(precondition)
    while precondition.find('(') != -1:
        action.precondition.append(make_predicate(parser.take_part(precondition)))
        precondition = parser.delete_part(precondition)

    effect = parser.take_part(text)
    text = parser.delete_part(text)
    if effect.find('(and ') != -1:
        action.quantifier_for_effect = 'and'
        effect = parser.take_part(effect)
    elif effect.find('(or ') != -1:
        action.quantifier_for_effect = 'or'
        effect = parser.take_part(effect)
    while effect.find('(') != -1:
        action.precondition.append(make_predicate(parser.take_part(effect)))
        effect = parser.delete_part(effect)

    return action


def make_predicate(text):
    predicate = fields.Predicate()

    if text.find('(not ') != -1:
        predicate.positively = False
        text = parser.take_part(text)

    text = text.split()

    predicate.name = text[0]

    param = fields.Parameter()

    for i in range(1, len(text)):
        if text[i] == '-':
            param.name = text[i - 1]
            param.name = text[i + 1]
            predicate.parameters.add(param)

    return predicate


def find_action(domain, name_action, methods):
    for i in domain.actions:
        if name_action == i.name:
            return i
    for i in domain.methods:
        if i.name == name_action:
            return i
    for i in methods:
        if i[0].find(':method ' + name_action) != -1 and i[1] == 0:
            method = make_method(domain, methods, i)
            domain.methods.add(method)
            return method
