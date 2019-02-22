import src.PDDL.domain as dom
import src.PDDL.parser as parser
import src.PDDL.fields as fields
import re


def make_domain(file):
    domain = dom.Domain()

    parsed_domain = parser.ParserForDomain(file)

    domain.name = re.sub(r'domain ', '', parsed_domain.name)

    domain.requirements = re.sub(r':requirements ', '', parsed_domain.requirements).split()

    domain.types = re.sub(r':types ', '', parsed_domain.types).split()

    domain.constants = re.sub(r':constants ', '', parsed_domain.constants).split()

    predicates = re.sub(r':predicates ', '', parsed_domain.predicates)
    while predicates.find(')') != -1:
        domain.predicates.append(fields.Predicate(parser.take_part(predicates)))
        predicates = parser.delete_part(predicates)

    for action in parsed_domain.actions:
        domain.actions.append(fields.Action(action, domain))

    define_methods(parsed_domain.methods, domain)

    return domain


def define_methods(methods, domain):
    names_of_methods = []
    for i in methods:
        names_of_methods.append([re.findall(r'\w+', (re.search(r':method [\w, -]+', i).group(0)))[1], False, i])
    for i in names_of_methods:
        if not i[1]:
            make_action_from_methods(i, names_of_methods, domain)


def make_action_from_methods(method, names, domain):
    # print(method)
    # print(names)
    # print(domain)
    # TODO: снова вопрос о и/или. Надо узнать нужен ли или вообще
    new_action = fields.Action()
    new_action.name = method[0]

    text = method[2]

    text_parameters = parser.take_part(text)
    parameters = re.findall(r'\?\w+ - \w+', text_parameters)
    for param in parameters:
        new_action.parameters.append([param.split()[0], param.split()[-1]])
    text = parser.delete_part(text)

    subgoals = take_tasks(parser.take_part(text))
    text = parser.delete_part(text)

    ordering = take_ordering(parser.take_part(text))
    text = parser.delete_part(text)

    order = 'init'
    goal_fluent = []
    precondition = []
    while order != 'goal':
        order = find_order(order, ordering)

        if order == 'goal':
            break
        eff = []
        action = find_action(domain, subgoals, order, names)
        pre, eff = fields.Action.action_for_method(action, find_order_action(order, subgoals)[2])
        precondition.append(pre)
        goal_fluent = fluent_for_goal(goal_fluent, eff)

    initial_fluent = fluent_for_initial(precondition, parameters)
    for i in goal_fluent:
        new_action.effect.append(i)
    for i in initial_fluent:
        new_action.precondition.append(i)
    domain.actions.append(new_action)
    method[1] = True
    for i in range(len(names)):
        if method[0] == names[i][0]:
            names[i][1] = True


def take_tasks(text):
    # TODO: сделал только для и. Или слишком легко, поэтому если надо будет добавлю.
    actions = []

    if re.search(r'and\s', text) is None:
        text = '(' + text + ')'
    while text.find('(') != -1:
        text_task = parser.take_part(text)
        name = re.search(r'[\w,-]+', text_task).group(0)

        text_task = parser.take_part(text_task)
        action = re.search(r'[\w,-]+', text_task).group(0)
        parameters = re.findall(r'\?\w+', text_task)

        actions.append([name, action, parameters])
        text = parser.delete_part(text)

    return actions


def take_ordering(text):
    # TODO: пока только и, потому что тут нетривиально :)
    ordering = []

    if re.search(r'and\s', text) is None:
        text = '(' + text + ')'

    while text.find('(') != -1:
        text_order = parser.take_part(text)

        order = text_order.split()
        order = [order[0], order[2]]
        ordering.append(order)

        text = parser.delete_part(text)
    return ordering


def find_order(name, ordering):
    for i in ordering:
        if i[0] == name:
            return i[1]


def find_order_action(order, subgoals):
    for i in subgoals:
        if i[0] == order:
            return i


def find_action(domain, subgoals, order, names):
    action = ''
    name_order_action = find_order_action(order, subgoals)[1]
    for i in domain.actions:
        if i.name == name_order_action:
            action = i
            break
    else:
        for i in names:
            if i[0] == name_order_action:
                make_action_from_methods(i, names, domain)
                print(subgoals)
                print(order)
                for j in domain.actions:
                    if j.name == name_order_action:
                        action = j
                        break
    return action


def fluent_for_goal(old_fluent, effects):
    for i in effects:
        for j in range(len(old_fluent)):
            eff = i
            if eff.find('(not ') != -1:
                eff = parser.take_part(parser.take_part(eff))
            if old_fluent[j].find(eff) != -1:
                old_fluent[j] = i
                break
        else:
            old_fluent.append(i)
    return old_fluent


def fluent_for_initial(pre, parameters):
    new_parameters = []
    preresult = []
    for i in parameters:
        new_parameters.append([re.search(r'\?\w+', i).group(0), True])
    for i in pre:
        for j in i:
            for y in new_parameters:
                if j.find(y[0]) != -1 and y[1]:
                    preresult.append(i)
                    y[1] = False
    result = set()
    for i in preresult:
        for j in i:
            result.add(j)
    return list(result)
