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


    return domain
